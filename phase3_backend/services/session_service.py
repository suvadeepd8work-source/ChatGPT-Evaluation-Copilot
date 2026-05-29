from sqlalchemy.orm import Session as DBSession
from models.session import Session
from datetime import datetime
import uuid

class SessionService:
    @staticmethod
    def get_or_create_session(db: DBSession, session_id: str = None, user_id: str = None):
        if session_id:
            session = db.query(Session).filter(Session.id == session_id).first()
            if session:
                return session
        
        # Create new session if not found or not provided
        new_session = Session(
            id=session_id or str(uuid.uuid4()),
            user_id=user_id or "anonymous",
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow()
        )
        db.add(new_session)
        db.commit()
        db.refresh(new_session)
        return new_session

    @staticmethod
    def update_session_activity(db: DBSession, session_id: str):
        session = db.query(Session).filter(Session.id == session_id).first()
        if session:
            session.updated_at = datetime.utcnow()
            db.commit()
            db.refresh(session)
        return session
