from pydantic import BaseModel, Field, field_validator


class SentimentAnalysisRequest(BaseModel):
    text: str = Field(..., min_length=1, description="Input text for sentiment analysis")

    @field_validator("text")
    @classmethod
    def validate_text_not_blank(cls, value: str) -> str:
        cleaned_value = value.strip()
        if not cleaned_value:
            raise ValueError("Text must not be empty or blank.")
        return cleaned_value


class SentimentAnalysisResponse(BaseModel):
    label: str = Field(..., description="Predicted sentiment label")
    score: float = Field(..., ge=0.0, le=1.0, description="Confidence score")
