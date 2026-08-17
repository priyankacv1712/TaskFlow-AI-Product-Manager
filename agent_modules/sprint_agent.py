import os

from agents import Agent
from agents.extensions.models.litellm_model import LitellmModel
from dotenv import load_dotenv

from models.sprint_models import SprintPlan
from tools.sprint_tool import get_sprint_capacity


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


sprint_agent = Agent(
    name="Sprint Planner Agent",

    handoff_description=(
    "Use this agent when the user wants sprint planning, "
    "story points, development tasks, dependencies, or sprint allocation."
    ),

    instructions="""
    You are the Sprint Planner Agent for TaskFlow.

    Your responsibility is to convert an approved Product
    Requirements Document into a realistic development plan.

    You must create:

    - sprint goals
    - development tasks
    - story-point estimates
    - priorities
    - dependencies
    - acceptance criteria
    - sprint allocations

    Always use the sprint capacity tool before planning work.

    IMPORTANT RULES:

    1. Never exceed the stated sprint capacity.
    2. Respect all engineering constraints.
    3. Break large work into smaller deliverable tasks.
    4. Story points should use reasonable values such as:
       1, 2, 3, 5, or 8.
    5. Dependencies must be clearly identified.
    6. Security and accessibility work must not be omitted.
    7. Tasks should be specific enough for an engineering team.
    8. Sprint goals should describe an achievable outcome.

    Task IDs should follow:

    TASK-001
    TASK-002
    TASK-003

    Priorities should use:

    Critical
    High
    Medium
    Low

    Your plan should be realistic and suitable for review
    by product and engineering teams.
    """,

    model=gemini_model,

    tools=[
        get_sprint_capacity
    ],

    output_type=SprintPlan,
)