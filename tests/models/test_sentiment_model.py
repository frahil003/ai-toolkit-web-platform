from app.models.sentiment_model import SentimentModel


def test_predict_returns_positive_for_positive_text() -> None:
    model = SentimentModel()

    label, score = model.predict("I love this amazing product.")

    assert label == "positive"
    assert score == 0.98


def test_predict_returns_negative_for_negative_text() -> None:
    model = SentimentModel()

    label, score = model.predict("This is the worst experience. I hate it.")

    assert label == "negative"
    assert score == 0.98


def test_predict_returns_neutral_for_text_without_keywords() -> None:
    model = SentimentModel()

    label, score = model.predict("The package arrived yesterday.")

    assert label == "neutral"
    assert score == 0.75


def test_predict_is_case_insensitive() -> None:
    model = SentimentModel()

    label, score = model.predict("I LOVE this product.")

    assert label == "positive"
    assert score == 0.98


def test_predict_returns_neutral_for_balanced_positive_and_negative_keywords() -> None:
    model = SentimentModel()

    label, score = model.predict("I love it, but I also hate the delay.")

    assert label == "neutral"
    assert score == 0.75