from fastapi import APIRouter

router = APIRouter()


@router.get("/ping", tags=["sentiment"])
def sentiment_ping() -> dict[str, str]:
	return {"message": "Sentiment endpoint is available"}
