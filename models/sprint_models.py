from pydantic import BaseModel


class SprintTask(BaseModel):
    task_id: str
    title: str
    description: str
    story_points: int
    priority: str
    dependencies: list[str]
    acceptance_criteria: list[str]


class Sprint(BaseModel):
    sprint_number: int
    sprint_goal: str
    capacity: int
    total_story_points: int
    tasks: list[SprintTask]


class SprintPlan(BaseModel):
    feature_name: str
    total_story_points: int
    number_of_sprints: int
    sprints: list[Sprint]
    planning_summary: str
    risks: list[str]