"""Model configuration — switch between Gemini, Groq, and Vertex via MODEL_PROVIDER env var.

Usage in agent files:
    from tutorials.model_config import get_model
    root_agent = Agent(model=get_model(), ...)

Providers:
  gemini (default) — AI Studio API, requires GOOGLE_API_KEY
  groq             — requires GROQ_API_KEY
  vertex           — Vertex AI with Application Default Credentials (ADC).
                     Requires:
                       1. `gcloud auth application-default login` (one-time)
                       2. GOOGLE_CLOUD_PROJECT and GOOGLE_CLOUD_LOCATION env vars
"""

import os


def get_model():
    provider = os.getenv("MODEL_PROVIDER", "gemini").lower()

    if provider == "groq":
        from google.adk.models.lite_llm import LiteLlm

        return LiteLlm(model=os.getenv("GROQ_MODEL", "groq/qwen/qwen3-32b"))

    if provider == "gemini":
        from google.adk.models.lite_llm import LiteLlm

        return LiteLlm(model=os.getenv("GEMINI_MODEL", "gemma-3-27b-it"))

    if provider == "vertex":
        # The ADK's built-in Gemini class is used when the model is a plain string.
        # It builds genai.Client() which reads these env vars and uses ADC:
        #   GOOGLE_GENAI_USE_VERTEXAI → route to aiplatform.googleapis.com
        #   GOOGLE_CLOUD_PROJECT, GOOGLE_CLOUD_LOCATION → target project/region
        # ADC comes from `gcloud auth application-default login` or a service account.
        os.environ.setdefault("GOOGLE_GENAI_USE_VERTEXAI", "True")
        return os.getenv("VERTEX_MODEL", "gemini-2.5-flash-lite")

    return os.getenv("GEMINI_MODEL", "gemma-3-27b-it")
