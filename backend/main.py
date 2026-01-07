from contextlib import asynccontextmanager
from typing import List

from dotenv import load_dotenv
from fastapi import Depends, FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from sqlalchemy import func, select
from sqlalchemy.orm import Session

# Load environment variables from .env file
load_dotenv()

from . import ai
from .database import Base, SessionLocal, engine
from .models import Review
from .schemas import (
    ReviewCreate,
    ReviewOut,
    ReviewsListResponse,
    StatsByRating,
    StatsData,
    StatsResponse,
    SubmitResponse,
    SubmitResponseData,
)


# Database setup
def init_db() -> None:
    Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    init_db()
    yield
    # Shutdown: nothing special


app = FastAPI(title="AI Feedback System", lifespan=lifespan)

# CORS (safe defaults for same-origin; can be extended if needed)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Static files (JS/CSS)
app.mount(
    "/static",
    StaticFiles(directory="frontend/static"),
    name="static",
)


@app.get("/", response_class=HTMLResponse)
async def user_dashboard() -> str:
    """Serve the public user dashboard (plain HTML + JS)."""
    with open("frontend/user.html", "r", encoding="utf-8") as f:
        return f.read()


@app.get("/admin", response_class=HTMLResponse)
async def admin_dashboard() -> str:
    """Serve the admin dashboard (plain HTML + JS)."""
    with open("frontend/admin.html", "r", encoding="utf-8") as f:
        return f.read()


@app.post("/api/reviews", response_model=SubmitResponse)
async def submit_review(
    payload: ReviewCreate, request: Request, db: Session = Depends(get_db)
) -> SubmitResponse:
    """
    Submit a review.
    - Validates rating (1–5) and review length.
    - Calls OpenRouter server-side for AI content.
    """
    try:
        rating = payload.rating
        review_text = (payload.review or "").strip()

        # Enforce max length defensively
        if len(review_text) > 5000:
            review_text = review_text[:5000]

        ai_result = await ai.generate_ai_content(rating=rating, review=review_text)

        review = Review(
            rating=rating,
            review=review_text,
            ai_response=ai_result["user_response"],
            ai_summary=ai_result["summary"],
            ai_recommended_actions=ai_result["recommended_actions"],
        )
        db.add(review)
        db.commit()
        db.refresh(review)

        return SubmitResponse(
            success=True,
            data=SubmitResponseData(
                id=review.id,
                rating=review.rating,
                review=review.review,
                ai_response=review.ai_response,
                created_at=review.created_at,
            ),
        )
    except HTTPException:
        raise
    except Exception as exc:  # noqa: BLE001
        print(f"[SUBMIT ERROR] {exc}")
        return SubmitResponse(
            success=False,
            error="Failed to submit review. Please try again.",
        )


@app.get("/api/reviews", response_model=ReviewsListResponse)
async def list_reviews(db: Session = Depends(get_db)) -> ReviewsListResponse:
    """
    Return all reviews (most recent first).
    """
    try:
        rows: List[Review] = (
            db.query(Review).order_by(Review.created_at.desc(), Review.id.desc()).all()
        )
        data = [
            ReviewOut(
                id=r.id,
                rating=r.rating,
                review=r.review,
                ai_response=r.ai_response,
                ai_summary=r.ai_summary,
                ai_recommended_actions=r.ai_recommended_actions,
                created_at=r.created_at,
            )
            for r in rows
        ]
        return ReviewsListResponse(success=True, data=data)
    except Exception as exc:  # noqa: BLE001
        print(f"[LIST ERROR] {exc}")
        return ReviewsListResponse(
            success=False,
            error="Failed to fetch reviews.",
        )


@app.get("/api/stats", response_model=StatsResponse)
async def get_stats(db: Session = Depends(get_db)) -> StatsResponse:
    """
    Return total count, counts per rating, and average rating.
    """
    try:
        total = db.query(func.count(Review.id)).scalar() or 0

        by_rating_raw = (
            db.query(Review.rating, func.count(Review.id))
            .group_by(Review.rating)
            .order_by(Review.rating)
            .all()
        )
        by_rating = [
            StatsByRating(rating=int(rating), count=int(count))
            for rating, count in by_rating_raw
        ]

        avg = db.query(func.avg(Review.rating)).scalar()
        average_rating = round(float(avg), 1) if avg is not None else 0.0

        data = StatsData(
            total=int(total),
            by_rating=by_rating,
            average_rating=average_rating,
        )
        return StatsResponse(success=True, data=data)
    except Exception as exc:  # noqa: BLE001
        print(f"[STATS ERROR] {exc}")
        return StatsResponse(
            success=False,
            error="Failed to fetch stats.",
        )


@app.get("/health")
async def health_check():
    return {"status": "ok"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("backend.main:app", host="0.0.0.0", port=8000, reload=True)

