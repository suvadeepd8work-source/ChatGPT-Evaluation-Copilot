from typing import List, Dict
from models.evaluation import StakeLevel

class AccountabilityService:
    """
    Generates human accountability reminders based on stake levels and confidence.
    """
    
    REMINDERS = {
        StakeLevel.LOW: "Verify any surprising information.",
        StakeLevel.MEDIUM: "Double-check key dates and names before sharing.",
        StakeLevel.HIGH: "MANDATORY: Verify all claims using primary sources. This response involves high-stakes information.",
        StakeLevel.CRITICAL: "CRITICAL: Do NOT act on this information without professional verification. AI-generated advice in this category can be dangerous."
    }

    def get_reminder(self, stake_level: StakeLevel, confidence_score: float) -> str:
        reminder = self.REMINDERS.get(stake_level, self.REMINDERS[StakeLevel.LOW])
        
        if confidence_score < 0.5:
            reminder += " Note: The AI has low confidence in this specific response."
            
        return reminder

    def get_verification_checklist(self, claims: List[str]) -> List[str]:
        return [f"Verify claim: {claim}" for claim in claims]

accountability_service = AccountabilityService()
