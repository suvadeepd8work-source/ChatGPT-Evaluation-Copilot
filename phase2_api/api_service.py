from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from loguru import logger
from groq_client import groq_client
from evaluation_parser import evaluation_parser

app = FastAPI(title="ChatGPT Evaluation Mode - Phase 2 API")

class EvalRequest(BaseModel):
    prompt: str
    stake_level: str = "medium"

def get_system_prompt(stake_level: str) -> str:
    base = """
    You are a critical AI Evaluator. Generate a response and a structural audit in JSON.
    Format:
    {
        "response": "Answer here",
        "claims": ["Claim 1", "Claim 2"],
        "confidence_score": 0.0-1.0,
        "limitations": "What you don't know",
        "potential_bias": "Bias detected",
        "verification_steps": ["Step 1"],
        "suggested_user_actions": ["Action 1"],
        "human_review_required": boolean
    }
    """
    if stake_level in ["high", "critical"]:
        base += "\nADVERSARIAL MODE: Be extremely skeptical. Flag all uncertainties."
    return base

@app.post("/evaluate")
async def evaluate(request: EvalRequest):
    try:
        system_prompt = get_system_prompt(request.stake_level)
        raw_response = await groq_client.call_groq(system_prompt, request.prompt)
        parsed_response = evaluation_parser.parse(raw_response)
        
        # High-risk override
        if request.stake_level in ["high", "critical"]:
            parsed_response["human_review_required"] = True
            
        return parsed_response
    except Exception as e:
        logger.error(f"Evaluation failed: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)
