from app.models.sentiment_model import SentimentModel
from app.services.sentiment_service import SentimentService


def get_sentiment_model() -> SentimentModel:
    return SentimentModel()


def get_sentiment_service() -> SentimentService:
    model = get_sentiment_model()
    return SentimentService(model=model)
