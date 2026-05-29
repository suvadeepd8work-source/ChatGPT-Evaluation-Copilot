import pytest
import asyncio
from unittest.mock import MagicMock, patch
from phase3_backend.services.orchestrator import EvaluationOrchestrator
from phase3_backend.models.evaluation import StakeLevel
from sqlalchemy.orm import Session

@pytest.fixture
def mock_db():
    return MagicMock(spec=Session)

@pytest.mark.asyncio
async def test_orchestrator_full_flow(mock_db):
    orchestrator = EvaluationOrchestrator()
    
    # Mock Groq client
    mock_response = MagicMock()
    mock_response.choices = [MagicMock()]
    mock_response.choices[0].message.content = '{"response": "Test response", "claims": ["Test claim"], "confidence_score": 0.9, "limitations": "None", "potential_bias": "None", "verification_steps": [], "suggested_user_actions": [], "human_review_required": false}'
    
    with patch.object(orchestrator.client.chat.completions, 'create', return_value=mock_response):
        # We need to mock SessionService too since it interacts with DB
        with patch('phase3_backend.services.orchestrator.SessionService') as mock_session_service:
            mock_session = MagicMock()
            mock_session.id = "test-session"
            mock_session_service.get_or_create_session.return_value = mock_session
            
            result = await orchestrator.process_request(
                mock_db, 
                prompt="Tell me about financial risks.",
                session_id="test-session"
            )
            
            assert result["response"] == "Test response"
            assert "evaluation" in result
            assert result["evaluation"]["accountability"]["human_review_required"] is True # Forced for financial (High Stake)
            assert mock_db.add.called
            assert mock_db.commit.called
