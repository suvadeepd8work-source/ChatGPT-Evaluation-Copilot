from typing import List, Dict
import re
from models.evaluation import IntentCategory, StakeLevel

class IntentClassifier:
    """
    Analyzes user prompts to categorize intent and determine stake levels.
    Phase 1 Requirement: Intent Taxonomy & Stakes Detection.
    """
    
    # Keywords mapped to Intent Categories
    INTENT_KEYWORDS = {
        IntentCategory.TECHNICAL: [
            "code", "debug", "function", "api", "architecture", "database", "sql", 
            "programming", "script", "algorithm", "deploy", "server"
        ],
        IntentCategory.FACTUAL: [
            "who is", "what is", "when did", "where is", "history", "tax", "law", 
            "medical", "symptoms", "diagnosis", "legal", "financial", "statistics", 
            "date", "event", "evidence", "proof"
        ],
        IntentCategory.SYNTHESIS: [
            "summarize", "condense", "key points", "extract", "abstract", "overview", 
            "tl;dr", "wrap up", "main ideas"
        ],
        IntentCategory.GENERATIVE: [
            "write a poem", "story", "creative", "brainstorm", "ideas", "social media", 
            "draft an email", "blog post", "hook", "inspiration"
        ]
    }

    # Keywords that immediately trigger High/Critical stakes
    HIGH_STAKES_KEYWORDS = [
        "medical", "doctor", "health", "symptoms", "medicine", "drug",
        "legal", "law", "court", "attorney", "contract", "lawyer",
        "tax", "irs", "financial", "investment", "money", "stock", "bank", "bitcoin", "crypto",
        "academic", "assignment", "essay", "thesis", "exam", "grade"
    ]

    def classify(self, prompt: str) -> Dict:
        prompt_lower = prompt.lower()
        
        # Determine Intent Category
        intent_scores = {category: 0 for category in IntentCategory}
        for category, keywords in self.INTENT_KEYWORDS.items():
            for word in keywords:
                if word in prompt_lower:
                    intent_scores[category] += 1
        
        # Default to GENERATIVE if no matches, else the highest score
        if all(score == 0 for score in intent_scores.values()):
            detected_intent = IntentCategory.GENERATIVE
        else:
            detected_intent = max(intent_scores, key=intent_scores.get)

        # Determine Stake Level
        stake_level = StakeLevel.LOW
        
        # Check for high-stakes keywords
        high_stakes_count = sum(1 for word in self.HIGH_STAKES_KEYWORDS if word in prompt_lower)
        
        if high_stakes_count > 0:
            stake_level = StakeLevel.HIGH
        elif detected_intent == IntentCategory.FACTUAL:
            stake_level = StakeLevel.MEDIUM
        elif detected_intent == IntentCategory.TECHNICAL:
            stake_level = StakeLevel.MEDIUM
        elif detected_intent == IntentCategory.SYNTHESIS:
            stake_level = StakeLevel.LOW
            
        # Critical override
        critical_keywords = ["emergency", "suicide", "poison", "fatal", "crime", "illegal"]
        if any(word in prompt_lower for word in critical_keywords):
            stake_level = StakeLevel.CRITICAL

        return {
            "intent": detected_intent,
            "stake_level": stake_level,
            "confidence": 0.85 # Static confidence for rule-based version
        }

intent_classifier = IntentClassifier()
