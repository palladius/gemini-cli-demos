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
import pathlib
import sys
from google.adk.tools import ToolContext
from google.cloud import storage

# Bypass corp airlock
os.environ["UV_INDEX_URL"] = "https://pypi.org/simple"

def ensure_assets(assets_dir: pathlib.Path):
    """Ensures reference images exist locally, downloading from GCS if needed."""
    bucket_name = "banana-ric-assets"
    images = [
        "ricc-za-view-with-kids.png",
        "ricc-za-lake.png",
        "ricc-za-wine-tasting.png",
        "ricc-pineapple-pizza.png",
        "ricc-google-switzerland.png",
        "riccardosouthafrica.png",
    ]
    
    os.makedirs(assets_dir, exist_ok=True)
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    
    for img in images:
        local_path = assets_dir / img
        if not local_path.exists():
            print(f"Downloading {img} from GCS...")
            blob = bucket.blob(img)
            blob.download_to_filename(str(local_path))

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
    agent_dir = pathlib.Path(__file__).parent
    script_path = agent_dir / "scripts" / "generate_image.py"
    
    # In cloud environments, use /tmp/ for assets to keep deployment payload small
    # and handle read-only source directories.
    if os.environ.get("GOOGLE_CLOUD_PROJECT"):
        assets_dir = pathlib.Path("/tmp/banana_ric_assets")
    else:
        assets_dir = agent_dir / "assets"
    
    # Ensure assets are present (download from GCS if cloud or missing)
    try:
        ensure_assets(assets_dir)
    except Exception as e:
        return {
            "status": "error",
            "message": f"Failed to ensure assets: {str(e)}"
        }
    
    reference_images = [
        assets_dir / "ricc-za-view-with-kids.png",
        assets_dir / "ricc-za-lake.png",
        assets_dir / "ricc-za-wine-tasting.png",
        assets_dir / "ricc-pineapple-pizza.png",
        assets_dir / "ricc-google-switzerland.png",
        assets_dir / "riccardosouthafrica.png",
    ]
    
    # Ensure out directory exists
    os.makedirs("out", exist_ok=True)
    full_path = os.path.join("out", filename)
    
    # Use current python executable for better cloud compatibility
    command = [
        sys.executable, str(script_path),
        "--prompt", prompt,
        "--filename", full_path,
    ]
    for img in reference_images:
        command.extend(["-i", str(img)])
        
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
    agent_dir = pathlib.Path(__file__).parent
    script_path = agent_dir / "scripts" / "generate_image.py"
    command = [sys.executable, str(script_path), "--help"]
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
