from pydantic import BaseModel


class FeatureMetricInsight(BaseModel):
    feature: str
    adoption_rate: float
    retention_rate: float
    performance_score: float
    status: str
    insight: str
    recommended_action: str


class ProductAnalyticsAnalysis(BaseModel):
    total_features_analysed: int
    overall_summary: str
    feature_insights: list[FeatureMetricInsight]
    highest_adoption_feature: str
    lowest_adoption_feature: str
    biggest_product_concern: str