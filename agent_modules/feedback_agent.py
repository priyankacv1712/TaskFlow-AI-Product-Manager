import os

from agents import Agent
from agents.extensions.models.litellm_model import LitellmModel
from dotenv import load_dotenv

from models.feedback_models import FeedbackAnalysis
from tools.feedback_tool import load_customer_feedback


load_dotenv()


gemini_api_key = os.getenv("GEMINI_API_KEY")

if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY was not found in the .env file.")


gemini_model = LitellmModel(
    model="gemini/gemini-3.5-flash-lite",
    api_key=gemini_api_key,
)


feedback_agent = Agent(
    name="Feedback Analysis Agent",

    handoff_description=(
        "Use this agent when the user wants customer feedback, "
        "complaints, sentiment, pain points, or feature requests analysed."
    ),

    instructions="""
    You are a specialist customer feedback analyst for TaskFlow,
    a SaaS project-management platform for small and medium businesses.

    Your responsibility is to analyse customer feedback and identify:

    - recurring themes
    - customer pain points
    - positive feedback
    - feature requests
    - sentiment
    - frequency of issues
    - severity of issues
    - recommended product actions

    You have access to a customer feedback tool.

    Always use the customer feedback tool when asked to analyse
    the TaskFlow customer feedback dataset.

    Base your analysis only on the feedback provided by the tool.
    Do not invent customer complaints or evidence.

    Severity should be scored from 1 to 5:

    1 = very low impact
    2 = low impact
    3 = moderate impact
    4 = high impact
    5 = critical impact

    For evidence, include short examples or summaries from the
    actual customer feedback.

    Identify the most important product issue at the end.
    """,

    model=gemini_model,

    tools=[
        load_customer_feedback
    ],

    output_type=FeedbackAnalysis,
)
