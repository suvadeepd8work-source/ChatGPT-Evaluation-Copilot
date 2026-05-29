import json
from datetime import datetime
from typing import List, Dict, Optional

class CertificationService:
    """
    Phase 5: Certified Output Generation.
    Produces a formal, human-verifiable summary of the AI interaction.
    """
    
    @staticmethod
    def generate_certified_output(
        interaction_id: str,
        response_text: str,
        verified_claims: List[str],
        unverified_claims: List[str],
        risk_summary: str,
        suggested_actions: List[str],
        accountability_statement: str
    ) -> Dict:
        certification = {
            "certification_id": f"CERT-{interaction_id[:8].upper()}",
            "timestamp": datetime.utcnow().isoformat(),
            "status": "Verified" if not unverified_claims else "Partially Verified",
            "content": {
                "original_response": response_text,
                "verification_status": {
                    "verified_claims": verified_claims,
                    "unverified_claims": unverified_claims,
                    "verification_rate": len(verified_claims) / (len(verified_claims) + len(unverified_claims)) if (len(verified_claims) + len(unverified_claims)) > 0 else 0
                },
                "risk_profile": {
                    "summary": risk_summary,
                    "suggested_next_steps": suggested_actions
                }
            },
            "legal_framework": {
                "accountability_statement": accountability_statement,
                "disclaimer": "This certification is based on human-in-the-loop verification of AI-generated claims."
            }
        }
        return certification

    @staticmethod
    def export_summary_json(certification: Dict, file_path: str):
        with open(file_path, 'w') as f:
            json.dump(certification, f, indent=4)
        return file_path

certification_service = CertificationService()
