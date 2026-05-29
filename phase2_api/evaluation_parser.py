import json
from typing import List, Dict, Any
from pydantic import BaseModel, Field, ValidationError
from loguru import logger

class EvaluationSchema(BaseModel):
    response: str
    claims: List[str]
    confidence_score: float = Field(ge=0, le=1)
    limitations: str
    potential_bias: str
    verification_steps: List[str]
    suggested_user_actions: List[str]
    human_review_required: bool

class EvaluationParser:
    """
    Parses and validates the structured JSON output from the Groq API.
    """
    @staticmethod
    def parse(json_str: str) -> Dict[str, Any]:
        try:
            data = json.loads(json_str)
            validated_data = EvaluationSchema(**data)
            return validated_data.model_dump()
        except json.JSONDecodeError as e:
            logger.error(f"Failed to decode JSON from Groq: {str(e)}")
            raise ValueError("Invalid JSON format from AI response")
        except ValidationError as e:
            logger.error(f"Failed to validate Groq output against schema: {str(e)}")
            raise ValueError("AI response does not match the required evaluation schema")

evaluation_parser = EvaluationParser()
