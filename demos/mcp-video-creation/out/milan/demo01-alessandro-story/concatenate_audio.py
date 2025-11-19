import os
import subprocess
import glob

def concatenate_folder(lang, chunks_dir, output_file):
    # Find all wav files
    search_path = os.path.join(chunks_dir, "*.wav")
    files = glob.glob(search_path)
    
    if not files:
        print(f"No files found in {chunks_dir}")
        return

    # Sort files to ensure correct order (01, 02, etc.)
    files.sort()
    
    print(f"Found {len(files)} chunks for {lang}:")
    for f in files:
        print(f" - {os.path.basename(f)}")

    # Create a temporary file list for ffmpeg
    list_file_path = os.path.join(chunks_dir, "files_to_concat.txt")
    with open(list_file_path, "w") as f:
        for file_path in files:
            # ffmpeg requires absolute paths or relative safe paths. 
            # escaping might be needed for special chars, but usually simple paths are fine.
            abs_path = os.path.abspath(file_path)
            f.write(f"file '{abs_path}'\n")

    # Run ffmpeg
    # ffmpeg -f concat -safe 0 -i mylist.txt -c copy output.wav
    cmd = [
        "ffmpeg",
        "-f", "concat",
        "-safe", "0",
        "-i", list_file_path,
        "-c", "copy",
        "-y", # Overwrite output
        output_file
    ]
    
    print(f"Concatenating to {output_file}...")
    try:
        subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(f"Successfully created {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"Error concatenating {lang}: {e.stderr.decode()}")
    finally:
        # Cleanup list file
        if os.path.exists(list_file_path):
            os.remove(list_file_path)

def main():
    base_dir = "out/milan/demo01-alessandro-story"
    chunks_base = os.path.join(base_dir, "audio-chunks")
    
    # English
    concatenate_folder(
        "en", 
        os.path.join(chunks_base, "en"), 
        os.path.join(base_dir, "story-en.wav")
    )
    
    # Italian
    concatenate_folder(
        "it", 
        os.path.join(chunks_base, "it"), 
        os.path.join(base_dir, "story-it.wav")
    )

if __name__ == "__main__":
    main()
