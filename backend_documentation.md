# Backend Documentation - Phase 3 Core

## Overview
The Phase 3 backend implements the core logic for the ChatGPT Evaluation Mode, focusing on structured evaluation, session management, and persistent auditing.

## Directory Structure
- `phase3_backend/`
  - `main.py`: Entry point for the FastAPI application.
  - `routes/`: API endpoint definitions.
    - `evaluation.py`: Handles AI processing and verification logging.
    - `sessions.py`: Manages user session lifecycle.
  - `services/`: Business logic and analysis engines.
    - `orchestrator.py`: The central brain coordinating AI calls and engine analysis.
    - `confidence_engine.py`: Calculates hybrid confidence scores.
    - `bias_engine.py`: Detects persuasive bias.
    - `tone_engine.py`: Analyzes stylistic vs clinical tone.
    - `accountability_service.py`: Generates human accountability reminders.
    - `session_service.py`: CRUD operations for sessions.
    - `verification_service.py`: Logs human verification actions.
  - `models/`: SQLAlchemy database models.
    - `base.py`: DB connection and session setup.
    - `session.py`: Session schema.
    - `interaction.py`: Interaction (prompt/response) schema.
    - `evaluation.py`: Detailed evaluation results schema.
    - `verification.py`: Audit trail for verification.
  - `storage/`: Local database storage (SQLite).
  - `utils/`: Configuration and shared utilities.
  - `middleware/`: Placeholder for future authentication and logging middleware.

## Key Features
### 1. Evaluation Orchestration
The `EvaluationOrchestrator` performs a single optimized call to the LLM (Groq) to get both the response and initial metadata. It then runs specialized local engines to refine the evaluation.

### 2. Confidence Scoring
A hybrid score (0.0-1.0) derived from:
- LLM internal certainty.
- Claim count grounding.
- Stake-based skepticism adjustments.

### 3. Bias & Tone Analysis
- **Bias Engine**: Identifies "authoritative fluff" and persuasive patterns.
- **Tone Engine**: Maps the emotional and clinical markers in the response.

### 4. Human Accountability
Integrated reminders that escalate based on stake level (Low to Critical), ensuring the user remains the Final Decision Maker (FDM).

### 5. Data Persistence
All interactions, evaluations, and human verification steps are logged in a SQLite database located at `phase3_backend/storage/evaluation.db`.

## API Endpoints
- `POST /api/v1/evaluation/process`: Main entry point for AI chat + evaluation.
- `POST /api/v1/evaluation/verify/{interaction_id}`: Logs a user verification action.
- `POST /api/v1/sessions/create`: Initializes a new session.
- `GET /api/v1/sessions/{session_id}`: Retrieves session history.

## Setup & Running
1. Install dependencies: `pip install -r requirements.txt`
2. Configure `.env` with `GROQ_API_KEY`.
3. Run: `python -m phase3_backend.main`
