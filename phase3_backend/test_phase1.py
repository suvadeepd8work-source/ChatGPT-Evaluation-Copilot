from services.intent_classifier import intent_classifier
from services.skepticism_calibrator import skepticism_calibrator
from services.de_biasing_service import de_biasing_service

test_prompts = [
    "Write a poem about the sea",
    "Summarize this tax law document for my returns",
    "Debug this python function for a medical database",
    "What is the fatal dose of this medicine?",
    "Clearly, it is a fact that this stock will definitely rise without a doubt."
]

for prompt in test_prompts:
    print(f"\n--- Testing Prompt: '{prompt}' ---")
    classification = intent_classifier.classify(prompt)
    calibration = skepticism_calibrator.calibrate(classification["stake_level"])
    tone = de_biasing_service.analyze_tone(prompt)
    
    print(f"Detected Intent: {classification['intent']}")
    print(f"Stake Level: {classification['stake_level']}")
    print(f"Friction Level: {calibration['friction']}")
    print(f"Persuasion Score: {tone['persuasion_score']:.2f}")
    if tone['is_highly_persuasive']:
        print("ALERT: Highly persuasive tone detected!")
        print(f"Stripped Tone: '{de_biasing_service.strip_tone(prompt)}'")
