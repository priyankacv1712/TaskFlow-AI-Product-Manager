from pydantic import BaseModel


class FeedbackInsight(BaseModel):
    theme: str
    sentiment: str
    frequency: int
    severity: int
    evidence: list[str]
    recommended_action: str


class FeedbackAnalysis(BaseModel):
    total_feedback_items: int
    overall_summary: str
    insights: list[FeedbackInsight]
    top_priority_issue: str
