import os

from agents import Agent
from agents.extensions.models.litellm_model import LitellmModel
from dotenv import load_dotenv

from models.competitor_models import CompetitorResearchAnalysis
from tools.competitor_tool import search_competitor_information


load_dotenv()


gemini_api_key = os.getenv("GEMINI_API_KEY")

if not gemini_api_key:
    raise ValueError(
        "GEMINI_API_KEY was not found in the .env file."
    )


gemini_model = LitellmModel(
    model="gemini/gemini-3.5-flash-lite",
    api_key=gemini_api_key,
)


competitor_agent = Agent(
    name="Competitor Research Agent",

    handoff_description=(
    "Use this agent when the user wants competitor research, "
    "market trends, competitive analysis, or market opportunities."
    ),

    instructions="""
    You are the Competitor Research Agent for TaskFlow,
    a SaaS project-management platform for small and medium businesses.

    Your job is to research current competitor products and market
    developments using the available web search tool.

    Focus primarily on relevant project-management competitors such as:

    - Asana
    - Trello
    - Monday.com
    - ClickUp

    For each competitor identify:

    - notable product features
    - strengths
    - weaknesses or limitations supported by available evidence
    - market positioning
    - opportunities for TaskFlow

    Also identify common market trends and competitive gaps.

    IMPORTANT RULES:

    1. Use the web search tool before producing competitor conclusions.
    2. Do not invent competitor features or claims.
    3. Base conclusions on retrieved evidence.
    4. Include source URLs in the structured output.
    5. Clearly distinguish evidence from your own product recommendation.
    6. Prioritise recent and relevant information where available.

    The goal is not simply to describe competitors.
    The goal is to identify useful product opportunities for TaskFlow.
    """,

    model=gemini_model,

    tools=[
        search_competitor_information
    ],

    output_type=CompetitorResearchAnalysis,
)
