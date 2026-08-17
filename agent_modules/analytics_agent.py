import os

from agents import Agent
from agents.extensions.models.litellm_model import LitellmModel
from dotenv import load_dotenv

from models.analytics_models import ProductAnalyticsAnalysis
from tools.analytics_tool import load_product_metrics


load_dotenv()


gemini_api_key = os.getenv("GEMINI_API_KEY")

if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY was not found in the .env file.")


gemini_model = LitellmModel(
    model="gemini/gemini-3.5-flash-lite",
    api_key=gemini_api_key,
)


analytics_agent = Agent(
    name="Product Analytics Agent",

    handoff_description=(
    "Use this agent when the user wants TaskFlow product metrics, "
    "feature adoption, retention, usage, engagement, or performance analysed."
    ),

    instructions="""
    You are the Product Analytics Agent for TaskFlow,
    a SaaS project-management platform.

    Your responsibility is to analyse actual product usage
    and performance data.

    You must examine:

    - feature adoption
    - monthly active users
    - weekly usage
    - retention
    - technical performance
    - underperforming features
    - high-performing features
    - potential product risks

    Always use the product metrics tool when asked to analyse
    TaskFlow product performance.

    Base your conclusions only on data returned by the tool.
    Do not invent metrics.

    For each feature, classify its status using one of:

    Strong
    Healthy
    Needs Attention
    Critical

    Consider multiple metrics when determining the status.

    Identify the biggest product concern based on the available
    analytics evidence and recommend practical product actions.
    """,

    model=gemini_model,

    tools=[
        load_product_metrics
    ],

    output_type=ProductAnalyticsAnalysis,
)
