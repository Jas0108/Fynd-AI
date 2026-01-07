from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, Text

from .database import Base


class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True)
    rating = Column(Integer, nullable=False, index=True)
    review = Column(Text, nullable=False, default="")
    ai_response = Column(Text, nullable=False)
    ai_summary = Column(Text, nullable=False)
    ai_recommended_actions = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False, index=True)

