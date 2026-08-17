from pydantic import BaseModel


class PrioritisedFeature(BaseModel):
    rank: int
    feature: str
    rice_score: float
    priority: str
    evidence: str
    reasoning: str
    recommended_action: str


class FeaturePrioritisationAnalysis(BaseModel):
    total_features_evaluated: int
    prioritised_features: list[PrioritisedFeature]
    top_priority_feature: str
    roadmap_summary: str