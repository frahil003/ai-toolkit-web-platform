from app.schemas.sentiment import (
    SentimentAnalysisRequest,
    SentimentAnalysisResponse,
)
from app.services.sentiment_service import SentimentService


class FakeSentimentModel:
    def predict(self, text: str) -> tuple[str, float]:
        return "positive", 0.91


class FakeNegativeSentimentModel:
    def predict(self, text: str) -> tuple[str, float]:
        return "negative", 0.87


class RecordingSentimentModel:
    def __init__(self) -> None:
        self.received_text: str | None = None

    def predict(self, text: str) -> tuple[str, float]:
        self.received_text = text
        return "neutral", 0.75


def test_analyze_returns_response_from_model() -> None:
    service = SentimentService(model=FakeSentimentModel())
    request = SentimentAnalysisRequest(text="This can be any text.")

    result = service.analyze(request)

    assert isinstance(result, SentimentAnalysisResponse)
    assert result.label == "positive"
    assert result.score == 0.91


def test_analyze_returns_negative_response_from_model() -> None:
    service = SentimentService(model=FakeNegativeSentimentModel())
    request = SentimentAnalysisRequest(text="Another test input.")

    result = service.analyze(request)

    assert result.label == "negative"
    assert result.score == 0.87


def test_analyze_passes_request_text_to_model() -> None:
    model = RecordingSentimentModel()
    service = SentimentService(model=model)
    request = SentimentAnalysisRequest(text="The package arrived yesterday.")

    result = service.analyze(request)

    assert model.received_text == "The package arrived yesterday."
    assert result.label == "neutral"
    assert result.score == 0.75