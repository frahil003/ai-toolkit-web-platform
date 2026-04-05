import logging

from app.models.sentiment_model import SentimentModel
from app.schemas.sentiment import (
    SentimentAnalysisRequest,
    SentimentAnalysisResponse,
)

logger = logging.getLogger(__name__)


class SentimentService:
    def __init__(self, model: SentimentModel | None = None) -> None:
        self.model = model or SentimentModel()

    def analyze(self, request: SentimentAnalysisRequest) -> SentimentAnalysisResponse:
        logger.info("Analyzing sentiment for incoming request.")

        label, score = self.model.predict(request.text)

        return SentimentAnalysisResponse(label=label, score=score)