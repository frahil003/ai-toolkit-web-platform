from fastapi import APIRouter

from app.schemas.sentiment import (
    SentimentAnalysisRequest,
    SentimentAnalysisResponse,
)
from app.services.sentiment_service import SentimentService

router = APIRouter()
sentiment_service = SentimentService()


@router.get("/ping", tags=["sentiment"])
def sentiment_ping() -> dict[str, str]:
    return {"message": "Sentiment endpoint is available"}


@router.post(
    "/analyze",
    response_model=SentimentAnalysisResponse,
    tags=["sentiment"],
)
def analyze_sentiment(
    request: SentimentAnalysisRequest,
) -> SentimentAnalysisResponse:
    return sentiment_service.analyze(request)
