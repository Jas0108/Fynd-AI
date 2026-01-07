from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, Field, conint


class ReviewCreate(BaseModel):
    rating: conint(ge=1, le=5) = Field(..., description="Rating from 1 to 5")
    review: Optional[str] = Field(
        default="",
        max_length=5000,
        description="Optional free-text review (up to 5000 characters)",
    )


class ReviewOut(BaseModel):
    id: int
    rating: int
    review: str
    ai_response: str
    ai_summary: str
    ai_recommended_actions: str
    created_at: datetime


class ReviewsListResponse(BaseModel):
    success: bool
    data: Optional[List[ReviewOut]] = None
    error: Optional[str] = None


class StatsByRating(BaseModel):
    rating: int
    count: int


class StatsData(BaseModel):
    total: int
    by_rating: List[StatsByRating]
    average_rating: float


class StatsResponse(BaseModel):
    success: bool
    data: Optional[StatsData] = None
    error: Optional[str] = None


class SubmitResponseData(BaseModel):
    id: int
    rating: int
    review: str
    ai_response: str
    created_at: datetime


class SubmitResponse(BaseModel):
    success: bool
    data: Optional[SubmitResponseData] = None
    error: Optional[str] = None

