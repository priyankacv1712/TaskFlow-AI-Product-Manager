from pydantic import BaseModel


class UserStory(BaseModel):
    title: str
    story: str
    acceptance_criteria: list[str]


class FunctionalRequirement(BaseModel):
    requirement_id: str
    requirement: str
    priority: str


class PRDDocument(BaseModel):
    product_name: str
    feature_name: str

    executive_summary: str
    problem_statement: str

    objectives: list[str]
    target_users: list[str]

    user_stories: list[UserStory]

    functional_requirements: list[FunctionalRequirement]
    non_functional_requirements: list[str]

    success_metrics: list[str]

    engineering_constraints: list[str]
    risks: list[str]
    dependencies: list[str]

    out_of_scope: list[str]

    launch_recommendation: str