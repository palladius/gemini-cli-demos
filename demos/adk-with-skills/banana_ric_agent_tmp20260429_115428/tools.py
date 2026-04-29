# Copyright 2026 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import subprocess
import os
from google.adk.tools import ToolContext

# Bypass corp airlock
os.environ["UV_INDEX_URL"] = "https://pypi.org/simple"

def generate_riccardo_image(prompt: str, filename: str) -> dict:
    """(DEPRECATED: uses direct subprocess call, not ADK-native skill integration)
    This is a temporary workaround until https://github.com/google/adk-python/issues/5524 is resolved.
    Generates an image of Riccardo using the nano-banana-ricc skill.
    This ensures character consistency for Riccardo.

    Args:
        prompt: A description of the image to generate, including Riccardo.
        filename: The name of the file to save the image to (should end in .png).

    Returns:
        A dict with 'status', 'message', and 'file_path'.
    """
    script_path = "/usr/local/google/home/ricc/.agents/skills/nano-banana-ricc/scripts/generate_image.py"
    assets_dir = "/usr/local/google/home/ricc/.agents/skills/nano-banana-ricc/assets/riccardo/"
    
    reference_images = [
        os.path.join(assets_dir, "ricc-za-view-with-kids.png"),
        os.path.join(assets_dir, "ricc-za-lake.png"),
        os.path.join(assets_dir, "ricc-za-wine-tasting.png"),
        os.path.join(assets_dir, "ricc-pineapple-pizza.png"),
        os.path.join(assets_dir, "ricc-google-switzerland.png"),
        os.path.join(assets_dir, "riccardosouthafrica.png"),
    ]
    
    # Ensure out directory exists
    os.makedirs("out", exist_ok=True)
    full_path = os.path.join("out", filename)
    
    command = [
        "uv", "run", script_path,
        "--prompt", prompt,
        "--filename", full_path,
    ]
    for img in reference_images:
        command.extend(["-i", img])
        
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        return {
            "status": "success",
            "message": f"Image generated successfully at {full_path}. Script output: {result.stdout}",
            "file_path": full_path
        }
    except subprocess.CalledProcessError as e:
        return {
            "status": "error",
            "message": f"Failed to generate image: {e.stderr}",
            "error": str(e)
        }

def get_nanobanana_help() -> dict:
    """Returns the help output of the nano-banana-ricc script.
    Use this to find out about available options like image size or resolution.

    Returns:
        A dict with 'status' and 'help_text'.
    """
    script_path = "/usr/local/google/home/ricc/.agents/skills/nano-banana-ricc/scripts/generate_image.py"
    command = ["uv", "run", script_path, "--help"]
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        return {
            "status": "success",
            "help_text": result.stdout
        }
    except subprocess.CalledProcessError as e:
        return {
            "status": "error",
            "message": f"Failed to get help: {e.stderr}"
        }
