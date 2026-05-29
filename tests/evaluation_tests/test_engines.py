import pytest
from phase3_backend.services.confidence_engine import confidence_engine
from phase3_backend.services.bias_engine import bias_engine
from phase3_backend.services.tone_engine import tone_engine
from phase3_backend.services.accountability_service import accountability_service
from phase3_backend.models.evaluation import StakeLevel

def test_confidence_scoring_high_stakes():
    # Test high-stakes query with low claim count
    score_data = confidence_engine.calculate_score(
        model_confidence=0.9,
        claims=[],
        stake_level=StakeLevel.HIGH
    )
    assert score_data["score"] < 0.9
    assert "Penalty: No verifiable claims" in score_data["reasoning"]

def test_confidence_scoring_critical_stakes():
    score_data = confidence_engine.calculate_score(
        model_confidence=0.95,
        claims=["Claim 1"],
        stake_level=StakeLevel.CRITICAL
    )
    assert score_data["score"] < 0.95
    assert "Skepticism Adjustment" in score_data["reasoning"]

def test_bias_detection_persuasive():
    text = "It is undoubtedly a fact that this is the best solution absolutely."
    bias_data = bias_engine.detect_bias(text)
    assert bias_data["bias_score"] > 0.5
    assert "undoubtedly" in bias_data["detected_patterns"]
    assert bias_data["is_highly_persuasive"] is True

def test_tone_analysis_clinical():
    text = "The research indicates that the evidence supports this data."
    tone_data = tone_engine.analyze_tone(text)
    assert tone_data["dominant_tone"] == "clinical"
    assert tone_data["clinical_index"] > 0.5

def test_accountability_reminders_critical():
    reminder = accountability_service.get_reminder(StakeLevel.CRITICAL, 0.4)
    assert "CRITICAL:" in reminder
    assert "low confidence" in reminder

def test_financial_risk_case():
    # Example case: "Should I invest all my savings into one cryptocurrency?"
    # 1. Stake detection (handled by intent_classifier in real flow, here we test service response)
    stake = StakeLevel.HIGH
    confidence = 0.85
    claims = ["Cryptocurrencies are volatile", "Diversification reduces risk"]
    
    reminder = accountability_service.get_reminder(stake, confidence)
    score_data = confidence_engine.calculate_score(confidence, claims, stake)
    
    assert "MANDATORY: Verify all claims" in reminder
    assert score_data["score"] < confidence # Due to high stake skepticism
