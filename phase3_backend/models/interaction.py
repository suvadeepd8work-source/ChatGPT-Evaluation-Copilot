from sqlalchemy import Column, String, DateTime, Text, ForeignKey, Float, JSON
from datetime import datetime
from models.base import Base
import uuid

class Interaction(Base):
    __tablename__ = "interactions"

    id = Column(String, primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    session_id = Column(String, ForeignKey("sessions.id"), index=True)
    user_prompt = Column(Text, nullable=False)
    ai_response = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Evaluation summary fields for quick access
    confidence_score = Column(Float)
    status = Column(String, default="completed") # e.g., pending, completed, failed
