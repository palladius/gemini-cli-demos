# Declarative Video Assembler: User Guide

This script provides a powerful, declarative workflow for assembling videos
from a simple YAML "plan". It uses ffmpeg to process and combine video clips,
add music and narration, and overlay text, creating a polished final video
without manual editing.

---

## Core Features

- **Declarative Workflow:** Define your entire video structure in a human-readable
  YAML file. Change a filename or a setting and simply re-run the script.
- **Scene-based Assembly:** Build your video from individual scene clips.
- **Audio Control:**
    - Add background music to any scene.
    - Overlay narration tracks and trim them to fit a scene's length.
    - Adjust music volume to avoid overpowering speech.
- **Text Overlays:** Burn text directly into your video scenes, with control
  over font, size, color, and position.
- **Automatic GIF Generation:** A high-quality, homonymous GIF is automatically
  created for every video produced.
- **Timeline Receipt:** After each successful assembly, a `.receipt.yaml` file
  is generated. This file is a copy of your plan, enriched with the exact
  start time, end time, and duration of each scene in the final video,
  providing a perfect, deterministic audit trail.

---

## Usage

```bash
python3 bin/assemble_video.py /path/to/your/video_plan.yaml
```

---

## The `video_plan.yaml` Structure

```yaml
# The title of your project
title: "My Awesome Video"

# The desired filename for the final output video
output_filename: "final_video.mp4"

# Global settings that apply to all scenes unless overridden
settings:
  music_volume_db: -15 # Default volume for music tracks in dB

# The list of scenes that make up your video
scenes:
  - scene: 1 # A unique identifier for the scene
    description: "A short description of the scene's content."
    video: "path/to/scene1.mp4" # The only required field for a scene

    # Add background music to this scene
    music:
      source: "path/to/music.wav"
      volume_db: -10 # Optional: overrides the global setting for this scene

    # Add a narration track to this scene
    narration:
      source: "path/to/full_narration.wav"
      start_time: 0   # Trim the narration from 0 seconds...
      end_time: 7.5   # ...to 7.5 seconds for this scene

    # Add a text overlay to this scene
    text_overlay:
      text: "Hello, World!"
      font_size: 48
      font_color: "white"
      # Position the text using ffmpeg's x and y expressions
      x: "(w-text_w)/2" # Centered horizontally
      y: "h-th-50"      # 50 pixels from the bottom

  - scene: 2
    description: "A scene with no music or narration."
    video: "path/to/scene2.mp4"
    # To omit a feature for a scene, set it to null or remove the key entirely
    music: null
    narration: null
```
