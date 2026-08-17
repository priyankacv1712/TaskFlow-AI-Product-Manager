import os

from agents import Agent
from agents.extensions.models.litellm_model import LitellmModel
from dotenv import load_dotenv

from agent_modules.feedback_agent import feedback_agent
from agent_modules.analytics_agent import analytics_agent
from agent_modules.competitor_agent import competitor_agent
from agent_modules.prioritisation_agent import prioritisation_agent
from agent_modules.prd_agent import prd_agent
from agent_modules.sprint_agent import sprint_agent
from tools.knowledge_tool import search_taskflow_knowledge


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


orchestrator_agent = Agent(
    name="Product Orchestrator Agent",

    instructions="""
    You are the central Product Orchestrator for TaskFlow.

    Your responsibility is to understand the Product Manager's
    request and hand the request to the most appropriate
    specialist agent.

    Available specialists:

    1. Feedback Analysis Agent
       Use for customer complaints, feedback, sentiment,
       pain points and feature requests.

    2. Product Analytics Agent
       Use for product usage, feature adoption, retention,
       engagement and performance metrics.

    3. Competitor Research Agent
       Use for competitor analysis, market research,
       market trends and competitive opportunities.

    4. Feature Prioritisation Agent
       Use for feature ranking, RICE scoring and roadmap
       prioritisation.

    5. PRD Writer Agent
       Use when an approved feature needs a Product
       Requirements Document.

    6. Sprint Planner Agent
       Use when approved requirements need to be converted
       into development tasks and sprint allocations.

    IMPORTANT RULES:

    - Do not perform specialist analysis yourself when a
      specialist agent is available.
    - Select the agent whose responsibility most closely
      matches the user's request.
    - Use handoffs to transfer control to the specialist.
    - Do not invent customer, analytics, competitor,
      roadmap or engineering evidence.
    - If the request concerns an important roadmap or
      development decision, remind the user that human
      approval is required before implementation.

    You also have access to TaskFlow's internal knowledge base.
    Use the knowledge retrieval tool when the user's request
    depends on internal product strategy, customer personas,
    company goals, engineering architecture, or product policies.
    
    Do not invent internal company information when it can be
    retrieved from the knowledge base.
    """,

    model=gemini_model,

    tools=[
    search_taskflow_knowledge,
    ],

    handoffs=[
        feedback_agent,
        analytics_agent,
        competitor_agent,
        prioritisation_agent,
        prd_agent,
        sprint_agent,
    ],
)