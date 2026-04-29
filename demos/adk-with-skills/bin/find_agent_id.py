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

import sys
from google.cloud import aiplatform

def get_agent_id(project, location, display_name):
    aiplatform.init(project=project, location=location)
    engines = aiplatform.ReasoningEngine.list()
    for engine in engines:
        if engine.display_name == display_name:
            # Resource name is in format projects/{project}/locations/{location}/reasoningEngines/{id}
            return engine.name.split('/')[-1]
    return None

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python find_agent_id.py <project> <location> <display_name>")
        sys.exit(1)
    
    project = sys.argv[1]
    location = sys.argv[2]
    display_name = sys.argv[3]
    
    agent_id = get_agent_id(project, location, display_name)
    if agent_id:
        print(agent_id)
    else:
        sys.exit(1)
