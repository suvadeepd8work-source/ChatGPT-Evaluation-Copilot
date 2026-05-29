from sqlalchemy.orm import Session as DBSession
from models.verification import VerificationAction
from datetime import datetime

class VerificationService:
    @staticmethod
    def log_verification(db: DBSession, interaction_id: str, action_type: str, details: dict):
        action = VerificationAction(
            interaction_id=interaction_id,
            action_type=action_type,
            details=details,
            status="logged",
            performed_at=datetime.utcnow()
        )
        db.add(action)
        db.commit()
        db.refresh(action)
        return action

verification_service = VerificationService()
