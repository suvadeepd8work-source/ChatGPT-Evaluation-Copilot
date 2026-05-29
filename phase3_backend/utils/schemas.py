from typing import List, Optional
from pydantic import BaseModel, Field

class EvaluationResponseSchema(BaseModel):
    response: str = Field(..., description="The primary answer to the user")
    claims: List[str] = Field(default_factory=list, description="Verifiable factual claims extracted from the response")
    confidence_score: float = Field(..., ge=0, le=1, description="Internal model certainty score")
    limitations: str = Field(..., description="Explicit statement of what the model doesn't know")
    potential_bias: str = Field(..., description="Identification of persuasive or prompt-echoing language")
    verification_steps: List[str] = Field(default_factory=list, description="Recommended actions for the user to confirm accuracy")
    suggested_user_actions: List[str] = Field(default_factory=list, description="Specific prompts or searches the user should perform")
    human_review_required: bool = Field(..., description="Flag for high-stakes or low-confidence content")

class OrchestrationRequest(BaseModel):
    prompt: str
    user_id: Optional[str] = None
    session_id: Optional[str] = None
