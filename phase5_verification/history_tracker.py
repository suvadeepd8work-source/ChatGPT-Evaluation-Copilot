from typing import List, Dict
from datetime import datetime

class HistoryTracker:
    """
    Phase 5: Verification History and Confidence Tracking.
    Tracks how confidence scores and verification status evolve over time.
    """
    
    def __init__(self):
        self.history = {} # interaction_id -> list of snapshots

    def log_snapshot(self, interaction_id: str, confidence_score: float, verified_count: int, total_claims: int):
        if interaction_id not in self.history:
            self.history[interaction_id] = []
            
        snapshot = {
            "timestamp": datetime.utcnow().isoformat(),
            "confidence_score": confidence_score,
            "verification_progress": {
                "verified": verified_count,
                "total": total_claims,
                "percentage": (verified_count / total_claims * 100) if total_claims > 0 else 0
            }
        }
        self.history[interaction_id].append(snapshot)
        return snapshot

    def get_interaction_trend(self, interaction_id: str) -> List[Dict]:
        return self.history.get(interaction_id, [])

history_tracker = HistoryTracker()
