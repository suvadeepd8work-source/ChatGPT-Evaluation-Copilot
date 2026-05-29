from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models.base import get_db
from services.session_service import SessionService

router = APIRouter(prefix="/sessions", tags=["sessions"])

@router.post("/create")
async def create_session(user_id: str = None, db: Session = Depends(get_db)):
    session = SessionService.get_or_create_session(db, user_id=user_id)
    return {"session_id": session.id, "user_id": session.user_id}

@router.get("/{session_id}")
async def get_session(session_id: str, db: Session = Depends(get_db)):
    session = SessionService.get_or_create_session(db, session_id=session_id)
    if not session:
        raise HTTPException(status_code=404, detail="Session not found")
    return session
