import json
from sqlalchemy.orm import Session as DBSession
from groq import Groq
from models.base import get_db
from models.interaction import Interaction
from models.evaluation import Evaluation, ConfidenceHistory
from models.session import Session as UserSession
from utils.config import settings
from services.confidence_engine import confidence_engine
from services.bias_engine import bias_engine
from services.tone_engine import tone_engine
from services.de_biasing_service import de_biasing_service
from services.accountability_service import accountability_service
from services.session_service import SessionService
from models.evaluation import StakeLevel, IntentCategory
from services.intent_classifier import intent_classifier
from utils.schemas import EvaluationResponseSchema

class EvaluationOrchestrator:
    def __init__(self):
        self.client = Groq(api_key=settings.GROQ_API_KEY)
        self.model = "llama-3.3-70b-versatile"

    async def process_request(self, db: DBSession, prompt: str, session_id: str = None, user_id: str = None):
        # 1. Session Management
        session = SessionService.get_or_create_session(db, session_id, user_id)
        
        # 2. Intent & Stake Classification
        classification = intent_classifier.classify(prompt)
        stake_level = classification["stake_level"]
        intent = classification["intent"]
        
        print(f"DEBUG: Processing request - Stake Level: {stake_level}, Intent: {intent}")

        # 3. AI Generation & Initial Evaluation (Single Call Strategy)
        system_prompt = self._generate_system_prompt(stake_level)
        completion = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt}
            ],
            response_format={"type": "json_object"},
            temperature=0.2,
        )
        
        ai_data = json.loads(completion.choices[0].message.content)
        print(f"DEBUG: AI Response received - Confidence: {ai_data.get('confidence_score')}")
        
        # 4. Engine Analysis
        conf_analysis = confidence_engine.calculate_score(
            ai_data["confidence_score"], 
            ai_data["claims"], 
            stake_level
        )
        
        bias_analysis = bias_engine.detect_bias(ai_data["response"])
        tone_analysis = tone_engine.analyze_tone(ai_data["response"])
        neutral_response = de_biasing_service.strip_tone(ai_data["response"])
        reminder = accountability_service.get_reminder(stake_level, conf_analysis["score"])

        # 5. Logging & Storage
        interaction = Interaction(
            session_id=session.id,
            user_prompt=prompt,
            ai_response=ai_data["response"],
            confidence_score=conf_analysis["score"]
        )
        db.add(interaction)
        db.commit()
        db.refresh(interaction)

        evaluation = Evaluation(
            interaction_id=interaction.id,
            claims=ai_data["claims"],
            limitations=ai_data["limitations"],
            confidence_score=conf_analysis["score"],
            bias_score=bias_analysis["bias_score"],
            bias_details=bias_analysis,
            tone_analysis=tone_analysis,
            human_review_required=ai_data["human_review_required"] or stake_level in [StakeLevel.HIGH, StakeLevel.CRITICAL],
            verification_steps=ai_data["verification_steps"],
            suggested_actions=ai_data["suggested_user_actions"]
        )
        db.add(evaluation)
        db.commit()
        db.refresh(evaluation)

        # Log confidence history
        conf_history = ConfidenceHistory(
            evaluation_id=evaluation.id,
            score=conf_analysis["score"],
            reasoning=conf_analysis["reasoning"]
        )
        db.add(conf_history)
        db.commit()

        # Update session activity
        SessionService.update_session_activity(db, session.id)

        # 6. Final Response Preparation
        return {
            "interaction_id": interaction.id,
            "session_id": session.id,
            "response": ai_data["response"],
            "neutral_response": neutral_response,
            "evaluation": {
                "claims": ai_data["claims"],
                "confidence": conf_analysis,
                "bias": bias_analysis,
                "tone": tone_analysis,
                "accountability": {
                    "reminder": reminder,
                    "human_review_required": evaluation.human_review_required
                },
                "verification_steps": ai_data["verification_steps"]
            }
        }

    def _generate_system_prompt(self, stake_level: StakeLevel) -> str:
        # Reusing logic from app/services/orchestrator.py
        base_prompt = """
        You are a highly critical AI Evaluation Assistant. Your goal is to provide COMPREHENSIVE and DETAILED responses 
        while explicitly identifying potential errors, biases, and areas requiring human verification.
        
        DO NOT provide brief or summarized answers. Provide a thorough explanation for the user's query.
        
        You MUST respond in valid JSON format matching this schema:
        {
            "response": "Your detailed and comprehensive answer here. Use Markdown for structure (headers, bolding, bullet points). Minimum 3-4 paragraphs.",
            "claims": ["Specific verifiable claim 1", "Specific verifiable claim 2", "Specific verifiable claim 3"],
            "confidence_score": 0.95,
            "limitations": "Detailed explanation of what you are unsure about or what the model lacks",
            "potential_bias": "Detailed analysis of any persuasive language or stylistic bias used",
            "verification_steps": ["Detailed step 1", "Detailed step 2", "Detailed step 3"],
            "suggested_user_actions": ["Specific action 1", "Specific action 2"],
            "human_review_required": false
        }
        
        STRUCTURE REQUIREMENTS for the 'response' field:
        1. Use '###' headers to separate sections (e.g., ### Overview, ### Analysis, ### Risks).
        2. Use bullet points ( - or * ) extensively for lists of facts, data, pros/cons, or key points to improve readability.
        3. Use **bolding** for emphasis on critical terms and data.
        4. Maintain an objective and clinical tone throughout.
        5. Ensure the response is detailed and well-elaborated (3-5 paragraphs total).
        
        IMPORTANT: Be objective and clinical. Avoid persuasive or flowery language. Maintain high factual density.
        """
        if stake_level in [StakeLevel.HIGH, StakeLevel.CRITICAL]:
            base_prompt += "\nADVERSARIAL MODE ENABLED: Be extremely skeptical. Highlight uncertainties. This is a HIGH STAKES request. Provide extra detail on risks and verification."
            
        return base_prompt

orchestrator = EvaluationOrchestrator()
