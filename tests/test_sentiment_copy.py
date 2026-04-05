from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_analyze_sentiment_positive() -> None:
    response = client.post(
        "/api/v1/sentiment/analyze",
        json={"text": "I love this product!"},
    )

    assert response.status_code == 200
    assert response.json() == {
        "label": "positive",
        "score": 0.98,
    }


def test_analyze_sentiment_negative() -> None:
    response = client.post(
        "/api/v1/sentiment/analyze",
        json={"text": "This is the worst experience. I hate it."},
    )

    assert response.status_code == 200
    assert response.json() == {
        "label": "negative",
        "score": 0.98,
    }


def test_analyze_sentiment_neutral() -> None:
    response = client.post(
        "/api/v1/sentiment/analyze",
        json={"text": "The package arrived yesterday."},
    )

    assert response.status_code == 200
    assert response.json() == {
        "label": "neutral",
        "score": 0.75,
    }


def test_analyze_sentiment_rejects_empty_text() -> None:
    response = client.post(
        "/api/v1/sentiment/analyze",
        json={"text": ""},
    )

    assert response.status_code == 422


def test_analyze_sentiment_rejects_blank_text() -> None:
    response = client.post(
        "/api/v1/sentiment/analyze",
        json={"text": "   "},
    )

    assert response.status_code == 422


def test_analyze_sentiment_rejects_missing_text() -> None:
    response = client.post(
        "/api/v1/sentiment/analyze",
        json={},
    )

    assert response.status_code == 422