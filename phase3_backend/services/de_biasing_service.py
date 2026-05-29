import re
from typing import List, Dict

class DeBiasingService:
    """
    Strips authoritative tone and separates truth from fluff.
    Phase 1 Requirement: Tone vs Truth analysis foundation.
    """
    
    # Adjectives and phrases that contribute to "Authoritative Tone"
    AUTHORITATIVE_PHRASES = [
        r"certainly", r"it is a fact that", r"undoubtedly", r"clearly",
        r"absolutely", r"of course", r"it is well known", r"everyone knows",
        r"without a doubt", r"definitely", r"truly", r"obviously"
    ]

    def analyze_tone(self, text: str) -> Dict:
        """
        Identifies authoritative phrases and calculates a 'Persuasion Score'.
        """
        matches = []
        for phrase in self.AUTHORITATIVE_PHRASES:
            found = re.findall(phrase, text, re.IGNORECASE)
            if found:
                matches.extend(found)
        
        word_count = len(text.split())
        persuasion_score = len(matches) / (word_count / 100) if word_count > 0 else 0
        
        return {
            "authoritative_phrases_found": list(set(matches)),
            "persuasion_score": min(1.0, persuasion_score / 10), # Normalized to 0-1
            "is_highly_persuasive": persuasion_score > 5
        }

    def strip_tone(self, text: str) -> str:
        """
        Removes authoritative phrases to present a more neutral version.
        """
        neutral_text = text
        for phrase in self.AUTHORITATIVE_PHRASES:
            neutral_text = re.sub(phrase + r"[, ]*", "", neutral_text, flags=re.IGNORECASE)
        
        # Capitalize first letter if it was removed
        if neutral_text:
            neutral_text = neutral_text[0].upper() + neutral_text[1:]
            
        return neutral_text.strip()

de_biasing_service = DeBiasingService()
