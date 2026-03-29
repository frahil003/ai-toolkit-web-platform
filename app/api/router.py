from fastapi import APIRouter

from app.api.v1 import sentiment

api_router = APIRouter()
api_router.include_router(sentiment.router, prefix="/sentiment")
