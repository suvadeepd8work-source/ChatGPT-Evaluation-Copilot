from typing import Dict
from models.evaluation import StakeLevel

class SkepticismCalibrator:
    """
    Sets the "Meaningful Friction" levels based on stakes and intent.
    Phase 1 Requirement: Skepticism Calibration Framework.
    """
    
    FRICTION_LEVELS = {
        StakeLevel.LOW: {
            "friction": "low",
            "actions": ["Highlight facts"],
            "blocks": [],
            "delay_ms": 0,
            "requires_signoff": False
        },
        StakeLevel.MEDIUM: {
            "friction": "medium",
            "actions": ["Highlight facts", "Prompt for missing context"],
            "blocks": [],
            "delay_ms": 2000,
            "requires_signoff": True
        },
        StakeLevel.HIGH: {
            "friction": "high",
            "actions": ["Adversarial prompting", "Forced source verification"],
            "blocks": ["Copy", "Share"],
            "delay_ms": 5000,
            "requires_signoff": True
        },
        StakeLevel.CRITICAL: {
            "friction": "adversarial",
            "actions": ["Hide authoritative language", "Forced evidence benchmarking"],
            "blocks": ["Copy", "Share", "Export"],
            "delay_ms": 10000,
            "requires_signoff": True
        }
    }

    def calibrate(self, stake_level: StakeLevel) -> Dict:
        return self.FRICTION_LEVELS.get(stake_level, self.FRICTION_LEVELS[StakeLevel.LOW])

skepticism_calibrator = SkepticismCalibrator()
