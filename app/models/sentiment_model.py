import logging

logger = logging.getLogger(__name__)


class SentimentModel:
    """Mock sentiment model for the first vertical slice."""

    POSITIVE_KEYWORDS = {
        "love",
        "great",
        "excellent",
        "awesome",
        "good",
        "happy",
        "amazing",
    }
    NEGATIVE_KEYWORDS = {
        "hate",
        "bad",
        "awful",
        "terrible",
        "worst",
        "sad",
        "poor",
    }

    def predict(self, text: str) -> tuple[str, float]:
        logger.info("Running mock sentiment inference.")

        normalized_text = text.lower()

        positive_matches = sum(
            keyword in normalized_text for keyword in self.POSITIVE_KEYWORDS
        )
        negative_matches = sum(
            keyword in normalized_text for keyword in self.NEGATIVE_KEYWORDS
        )

        if positive_matches > negative_matches:
            return "positive", 0.98

        if negative_matches > positive_matches:
            return "negative", 0.98

        return "neutral", 0.75