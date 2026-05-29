from sqlalchemy import Column, String, DateTime, Text, ForeignKey, JSON
from datetime import datetime
from models.base import Base
import uuid

class VerificationAction(Base):
    __tablename__ = "verification_actions"

    id = Column(String, primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    interaction_id = Column(String, ForeignKey("interactions.id"), index=True)
    
    action_type = Column(String) # e.g., "link_click", "search", "manual_confirm"
    details = Column(JSON)
    status = Column(String) # e.g., "verified", "flagged", "pending"
    
    performed_at = Column(DateTime, default=datetime.utcnow)
