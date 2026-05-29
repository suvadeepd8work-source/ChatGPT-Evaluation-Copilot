from typing import Dict, List, Optional
from datetime import datetime
import uuid

class FeedbackService:
    """
    Phase 5: Hallucination Reporting and User Feedback Loop.
    Allows users to flag errors and provide feedback on AI evaluation accuracy.
    """
    
    def __init__(self):
        self.feedback_store = [] # In-memory store for prototype, would be DB in production

    def report_hallucination(self, interaction_id: str, claim_text: str, user_evidence: str) -> Dict:
        report = {
            "report_id": str(uuid.uuid4()),
            "interaction_id": interaction_id,
            "type": "hallucination",
            "flagged_claim": claim_text,
            "user_provided_evidence": user_evidence,
            "timestamp": datetime.utcnow().isoformat(),
            "status": "pending_review"
        }
        self.feedback_store.append(report)
        print(f"HALLUCINATION REPORTED: Interaction {interaction_id} - Claim: {claim_text}")
        return report

    def submit_general_feedback(self, interaction_id: str, rating: int, comments: str) -> Dict:
        feedback = {
            "feedback_id": str(uuid.uuid4()),
            "interaction_id": interaction_id,
            "rating": rating, # 1-5
            "comments": comments,
            "timestamp": datetime.utcnow().isoformat()
        }
        self.feedback_store.append(feedback)
        return feedback

    def get_history(self, interaction_id: str) -> List[Dict]:
        return [f for f in self.feedback_store if f.get("interaction_id") == interaction_id]

feedback_service = FeedbackService()
