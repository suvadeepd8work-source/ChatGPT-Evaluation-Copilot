import re
from typing import List, Dict

class BiasDetectionEngine:
    """
    Identifies persuasive or prompt-echoing language.
    """
    
    PERSUASIVE_PATTERNS = [
        r"certainly", r"undoubtedly", r"clearly", r"obviously",
        r"it is well known", r"everyone knows", r"without a doubt",
        r"definitely", r"truly", r"absolutely", r"it is a fact that"
    ]

    def detect_bias(self, text: str) -> Dict:
        matches = []
        for pattern in self.PERSUASIVE_PATTERNS:
            found = re.findall(pattern, text, re.IGNORECASE)
            if found:
                matches.extend(found)
        
        word_count = len(text.split())
        bias_intensity = len(matches) / (word_count / 100) if word_count > 0 else 0
        
        # Normalize to 0-1
        normalized_score = min(1.0, bias_intensity / 10)
        
        return {
            "bias_score": normalized_score,
            "detected_patterns": list(set(matches)),
            "is_highly_persuasive": bias_intensity > 5,
            "recommendation": "Review highlighted persuasive language for potential bias." if normalized_score > 0.3 else "Neutral tone detected."
        }

bias_engine = BiasDetectionEngine()
