from typing import List, Dict
from models.evaluation import StakeLevel

class ConfidenceScoringEngine:
    """
    Calculates a hybrid confidence score based on model certainty, 
    source grounding, and reasoning depth.
    """
    
    def calculate_score(self, model_confidence: float, claims: List[str], stake_level: str) -> Dict:
        # Simple hybrid logic for now:
        # 1. Base score from model confidence
        # 2. Penalty for lack of claims in high-stakes
        # 3. Penalty for high-stakes in general (higher skepticism)
        
        score = model_confidence
        reasoning = []
        
        reasoning.append(f"Base model confidence: {model_confidence:.2f}")
        
        # Claim grounding check
        if len(claims) == 0 and stake_level in [StakeLevel.HIGH, StakeLevel.CRITICAL]:
            score -= 0.2
            reasoning.append("Penalty: No verifiable claims provided for high-stakes query.")
        elif len(claims) > 0:
            score += 0.05
            reasoning.append(f"Bonus: {len(claims)} verifiable claims identified.")
            
        # Stake-based skepticism
        if stake_level == StakeLevel.CRITICAL:
            score -= 0.15
            reasoning.append("Skepticism Adjustment: Critical stake level requires extreme caution.")
        elif stake_level == StakeLevel.HIGH:
            score -= 0.1
            reasoning.append("Skepticism Adjustment: High stake level requires additional verification.")
            
        # Ensure score is within 0-1
        final_score = max(0.0, min(1.0, score))
        
        return {
            "score": final_score,
            "reasoning": "; ".join(reasoning)
        }

confidence_engine = ConfidenceScoringEngine()
