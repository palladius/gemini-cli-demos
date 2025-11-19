import os
import subprocess

ROOT_DIR = "/Users/ricc/git/gemini-cli-demos/demos/mcp-video-creation"
TARGET_DIR = os.path.join(ROOT_DIR, "out/pescara")
NOT_ADDED_FILE = os.path.join(ROOT_DIR, "NOT_ADDED.md")
MAX_SIZE_BYTES = 10 * 1024 * 1024 # 10MB

to_add = []
not_added = []

if not os.path.exists(TARGET_DIR):
    print(f"Error: {TARGET_DIR} does not exist.")
    exit(1)

for root, dirs, files in os.walk(TARGET_DIR):
    for file in files:
        filepath = os.path.join(root, file)
        # Skip .DS_Store
        if file == ".DS_Store":
            continue
            
        size = os.path.getsize(filepath)
        
        if size > MAX_SIZE_BYTES:
            not_added.append(filepath)
        else:
            to_add.append(filepath)

print(f"Found {len(to_add)} files to add.")
print(f"Found {len(not_added)} files too large to add.")

# Git add
if to_add:
    # Batch add to avoid command line length limits
    # Using -f to force add ignored files
    chunk_size = 50
    for i in range(0, len(to_add), chunk_size):
        chunk = to_add[i:i+chunk_size]
        cmd = ["git", "add", "-f"] + chunk
        try:
            subprocess.run(cmd, cwd=ROOT_DIR, check=True)
            print(f"Added chunk {i//chunk_size + 1}")
        except subprocess.CalledProcessError as e:
            print(f"Error adding chunk: {e}")

# Write NOT_ADDED.md
with open(NOT_ADDED_FILE, "w") as f:
    f.write("# Files Not Added (Too Large > 10MB)\n\n")
    for path in sorted(not_added):
        rel_path = os.path.relpath(path, ROOT_DIR)
        size_mb = os.path.getsize(path) / (1024*1024)
        f.write(f"- `{rel_path}` ({size_mb:.2f} MB)\n")

print(f"Written {NOT_ADDED_FILE}")
