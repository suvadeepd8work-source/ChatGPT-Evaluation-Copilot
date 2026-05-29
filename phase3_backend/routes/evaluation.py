from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models.base import get_db
from services.orchestrator import orchestrator
from services.verification_service import verification_service
from utils.schemas import OrchestrationRequest

router = APIRouter(prefix="/evaluation", tags=["evaluation"])

@router.post("/process")
async def process_evaluation(request: OrchestrationRequest, db: Session = Depends(get_db)):
    try:
        result = await orchestrator.process_request(
            db, 
            request.prompt, 
            request.session_id, 
            request.user_id
        )
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/verify/{interaction_id}")
async def log_verification(interaction_id: str, action: dict, db: Session = Depends(get_db)):
    try:
        return verification_service.log_verification(
            db, 
            interaction_id, 
            action.get("type"), 
            action.get("details")
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
