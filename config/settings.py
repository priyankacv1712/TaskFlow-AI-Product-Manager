import os

from dotenv import load_dotenv
from agents import set_tracing_disabled
from agents.extensions.models.litellm_model import LitellmModel


load_dotenv()


# We use Gemini through LiteLLM, so OpenAI trace export
# is disabled to avoid unnecessary trace-export warnings.
set_tracing_disabled(True)


GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

MODEL_NAME = "gemini/gemini-3.5-flash-lite"


if not GEMINI_API_KEY:
    raise ValueError(
        "GEMINI_API_KEY was not found in the .env file."
    )


gemini_model = LitellmModel(
    model=MODEL_NAME,
    api_key=GEMINI_API_KEY,
)