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

import os
from google.adk.agents import Agent
from google.adk.apps.app import App
from google.adk.models.llm_response import LlmResponse
from google.adk.plugins.base_plugin import BasePlugin
from google.adk.plugins.multimodal_tool_results_plugin import MultimodalToolResultsPlugin
from google.genai import types, errors as genai_errors
from .tools import generate_riccardo_image, get_nanobanana_help

# Bypass corp airlock
os.environ["UV_INDEX_URL"] = "https://pypi.org/simple"
os.environ["GOOGLE_CLOUD_AGENT_ENGINE_ENABLE_TELEMETRY"] = "true"
os.environ["OTEL_INSTRUMENTATION_GENAI_CAPTURE_MESSAGE_CONTENT"] = "true"

class ErrorHandlingPlugin(BasePlugin):
    """Gracefully handles 503/UNAVAILABLE and 429/QUOTA errors from the LLM."""
    def __init__(self):
        super().__init__(name="error_handling_plugin")

    async def on_model_error_callback(self, *, callback_context, llm_request, error) -> LlmResponse | None:
        if isinstance(error, genai_errors.ServerError) and "503" in str(error):
            return LlmResponse(
                content=types.Content(
                    role="model",
                    parts=[types.Part.from_text(text="Ouch! The model is feeling a bit 'slipped up' right now (503 High Demand). 🍌 Let's wait a few seconds and try again. Don't worry, Banana Ric never gives up!")]
                )
            )
        if isinstance(error, genai_errors.ClientError) and "429" in str(error):
             return LlmResponse(
                content=types.Content(
                    role="model",
                    parts=[types.Part.from_text(text="Slow down there, partner! 🍌 We've hit a quota limit (429). Let's take a tiny banana break and try again in a minute!")]
                )
            )
        return None

root_agent = Agent(
    name="banana_ric_agent",
    model="gemini-3-flash-preview",
    instruction="""You are Banana Ric, an agent with Character Consistency capabilities for Riccardo.
    You can generate images of Riccardo doing various crazy stuff.
    You have access to the nano-banana-ricc skill to generate images while preserving character consistency.
    You can also provide help regarding the script's options.
    If the user asks to generate an image, use the generate_riccardo_image tool.
    If the user asks about script options or help, use the get_nanobanana_help tool.
    Always be polite and enthusiastic about generating images of Riccardo!""",
    tools=[generate_riccardo_image, get_nanobanana_help]
)

app = App(
    name="banana_ric_app",
    root_agent=root_agent,
    plugins=[ErrorHandlingPlugin()]
)
