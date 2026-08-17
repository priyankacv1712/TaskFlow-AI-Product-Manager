from pydantic import BaseModel


class CompetitorInsight(BaseModel):
    competitor_name: str
    strengths: list[str]
    weaknesses: list[str]
    notable_features: list[str]
    market_position: str
    opportunity_for_taskflow: str
    sources: list[str]


class CompetitorResearchAnalysis(BaseModel):
    competitors_analysed: int
    overall_market_summary: str
    competitor_insights: list[CompetitorInsight]
    common_market_trends: list[str]
    biggest_competitive_gap: str
    recommended_product_opportunity: str
