from sqlalchemy import Column, String, DateTime, Text, ForeignKey, Float, JSON, Boolean
from datetime import datetime
from models.base import Base
import uuid

from enum import Enum

class IntentCategory(str, Enum):
    GENERATIVE = "generative"
    SYNTHESIS = "synthesis"
    TECHNICAL = "technical"
    FACTUAL = "factual"

class StakeLevel(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"

class Evaluation(Base):
    __tablename__ = "evaluations"

    id = Column(String, primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    interaction_id = Column(String, ForeignKey("interactions.id"), index=True)
    
    # Metadata
    claims = Column(JSON) # List of claims
    limitations = Column(Text)
    
    # Engines results
    confidence_score = Column(Float)
    bias_score = Column(Float)
    bias_details = Column(JSON)
    tone_analysis = Column(JSON)
    
    # Accountability
    human_review_required = Column(Boolean, default=False)
    verification_steps = Column(JSON)
    suggested_actions = Column(JSON)
    
    created_at = Column(DateTime, default=datetime.utcnow)

class ConfidenceHistory(Base):
    __tablename__ = "confidence_history"
    
    id = Column(String, primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    evaluation_id = Column(String, ForeignKey("evaluations.id"), index=True)
    score = Column(Float)
    reasoning = Column(Text)
    timestamp = Column(DateTime, default=datetime.utcnow)
