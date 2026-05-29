from typing import Dict
import re

class ToneAnalysisEngine:
    """
    Separates the "persuasive" style (tone) from the "verifiable" claims (truth).
    """
    
    TONE_MARKERS = {
        "authoritative": [r"must", r"should", r"always", r"never", r"guaranteed"],
        "empathetic": [r"understand", r"feel", r"sorry", r"help", r"support"],
        "clinical": [r"evidence", r"study", r"data", r"research", r"indicates"],
        "uncertain": [r"maybe", r"possibly", r"suggests", r"could", r"might"]
    }

    def analyze_tone(self, text: str) -> Dict:
        text_lower = text.lower()
        results = {}
        
        for tone, patterns in self.TONE_MARKERS.items():
            count = 0
            for pattern in patterns:
                count += len(re.findall(pattern, text_lower))
            results[tone] = count
            
        dominant_tone = max(results, key=results.get) if any(results.values()) else "neutral"
        
        return {
            "tone_breakdown": results,
            "dominant_tone": dominant_tone,
            "clinical_index": results["clinical"] / (sum(results.values()) or 1)
        }

tone_engine = ToneAnalysisEngine()
