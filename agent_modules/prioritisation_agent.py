import os

from tools.approval_tool import approve_product_feature
from agents import Agent
from agents.extensions.models.litellm_model import LitellmModel
from dotenv import load_dotenv
from tools.knowledge_tool import search_taskflow_knowledge

from models.prioritisation_models import (
    FeaturePrioritisationAnalysis,
)
from tools.prioritisation_tool import (
    calculate_feature_priorities,
)


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


prioritisation_agent = Agent(
    name="Feature Prioritisation Agent",

    handoff_description=(
    "Use this agent when the user wants features ranked, "
    "prioritised, scored, or turned into a product roadmap."
    ),

    instructions="""
    You are the Feature Prioritisation Agent for TaskFlow.

    Your role is to evaluate proposed product improvements and
    produce an evidence-based product roadmap.

    You have access to a tool that loads feature candidates and
    calculates their RICE-style priority scores.

    Always use the prioritisation tool before making a decision.

    The score is calculated using:

    (Reach × Impact × Confidence) / Effort

    Higher scores indicate stronger priority based on the
    supplied evidence and estimates.

    When analysing the results:

    - preserve the calculated RICE score
    - consider the supporting evidence
    - explain why each feature matters
    - assign a roadmap priority
    - recommend an appropriate product action

    Use these priority labels:

    Critical
    High
    Medium
    Low

    The highest RICE score should normally receive the highest
    ranking unless there is a clearly stated evidence-based reason
    otherwise.

    Do not invent customer evidence, metrics or feature candidates.

    Rank every supplied feature from highest to lowest priority.

    Your goal is to produce a roadmap that a Product Manager could
    use for planning.

    After selecting the top-priority feature, call the
    approve_product_feature tool before treating the feature
    as approved for PRD or sprint planning.
    
    Do not claim that the feature is approved unless the
    human approval tool has actually been approved.

    Use the internal knowledge base when relevant to check
    TaskFlow product strategy, business goals and product
    policies before finalising roadmap recommendations.
    """,

    model=gemini_model,

    tools=[
        calculate_feature_priorities,
        search_taskflow_knowledge,
        approve_product_feature,
    ],

    output_type=FeaturePrioritisationAnalysis,
)

