# Detailed System Architecture: ChatGPT Evaluation Mode

## 1. Overview
The "ChatGPT Evaluation Mode" is a multi-layered system designed to provide a critical interface between users and AI models. It focuses on de-biasing, factual verification, and human accountability.

---

## 2. Architecture Layers

### **Research Layer**
- **Location**: `data/research/`
- **Function**: Stores and processes qualitative and quantitative research data.
- **Components**:
    - `Survey Processor`: Analyzes user trust levels and verification habits.
    - `Interview Synthesizer`: Extracts recurring themes and trust breakdown moments.
    - `Persona Manager`: Maps system behavior to specific user risk profiles.

### **Evaluation Orchestration Layer**
- **Function**: The central brain of the system.
- **Responsibilities**:
    - **Single-Call Performance**: Coordinates with LLMs to generate response and evaluation data in a single request.
    - **Engine Routing**: Pipes AI data through localized engines (Confidence, Bias, Tone) without additional LLM calls.
    - **Meaningful Friction**: Calibrates UI speed based on intent stakes to prevent passive acceptance.

### **Performance Architecture**
- **Orchestration**: Single-pass LLM execution for ~60% faster response times.
- **State Management**: Zustand-powered atomic updates in the frontend to minimize re-renders.
- **Data Persistence**: Async database logging to ensure UI responsiveness.

### **Groq API Layer**
- **Location**: `phase2_api/`
- **Function**: High-speed, optimized inference using `llama-3.3-70b-versatile`.
- **Components**:
    - `groq_client.py`: Handles API connection, tenacity-based retries, and error handling.
    - `evaluation_parser.py`: Enforces Pydantic-based schema validation for AI responses.
    - `api_service.py`: FastAPI implementation for the evaluation microservice.
- **Responsibilities**:
    - **Single-Call Optimization**: Generates both the primary response and the comprehensive evaluation in one request to minimize latency.
    - **Structured Output**: Enforces a strict JSON schema for all evaluation data.
    - **Dynamic Prompting**: Adjusts system instructions based on the detected stake level (High-risk queries trigger stronger adversarial evaluation).

### **Evaluation Response Schema (JSON)**
All AI interactions are structured to include:
- `response`: The primary answer to the user.
- `claims`: List of verifiable factual claims extracted from the response.
- `confidence_score`: 0-1 score reflecting internal model certainty.
- `limitations`: Explicit statement of what the model doesn't know.
- `potential_bias`: Identification of persuasive or prompt-echoing language.
- `verification_steps`: Recommended actions for the user to confirm accuracy.
- `suggested_user_actions`: Specific prompts or searches the user should perform.
- `human_review_required`: Boolean flag (True for high-stakes/low-confidence).

### **Confidence Scoring System**
- **Logic**: A hybrid score derived from:
    - `Model Consensus`: Agreement between multiple LLMs.
    - `Source Grounding`: Availability and reliability of external citations.
    - `Reasoning Depth`: Analysis of the Chain-of-Thought (CoT) logic.

### **Bias Detection & Tone vs. Truth System**
- **Bias Detection**: Identifies manipulative language or prompt-echoing.
- **Tone vs. Truth**: A clinical analyzer that separates the "persuasive" style (tone) from the "verifiable" claims (truth).

### **Verification & Hallucination Workflow (Phase 5)**
- **Location**: `phase5_verification/`
- **Source Auditor**: Real-time checks for URLs, DOIs, and book titles.
- **Hallucination Reporting**: Users can flag specific AI claims as "hallucinated" and provide counter-evidence.
- **Certified Output**: Generates a formal "AI Certification" document summarizing verified vs. unverified claims and human accountability.
- **History Tracker**: Monitors the evolution of confidence scores as human verification progress increases.

---

## 3. Technical Architecture

### **Backend Layer (Phase 3 Core)**
- **Location**: `phase3_backend/`
- **Function**: Handles session management, evaluation orchestration, and data persistence.
- **Components**:
    - `Orchestrator`: Coordinates calls between LLMs and specialized analysis engines.
    - `Confidence Engine`: Hybrid scoring system for model certainty.
    - `Bias Engine`: Detects persuasive and prompt-echoing language.
    - `Tone Engine`: Separates authoritative tone from verifiable truth.
    - `Accountability Service`: Generates human-centric reminders and verification checklists.
    - `Session Service`: Manages user sessions and interaction history.
- **Persistence**:
    - `interactions`: Logs of prompts and responses.
    - `evaluations`: Detailed metadata, scores, and analysis results.
    - `verification_actions`: Audit trail of human verification steps.
    - `confidence_history`: Temporal tracking of confidence score evolution.

### **Frontend Layer (Phase 4 Prototype)**
- **Location**: `phase4_frontend/`
- **Tech Stack**: React, Tailwind CSS, Zustand, Lucide.
- **Key UI/UX Features**:
    - **Dual-Pane Interface**: Chat area vs. Evidence Bench.
    - **Evaluation Toggle**: Modes for "Standard" (standard chat) and "Evaluation" (critical analysis).
    - **Confidence Heatmap**: Visual feedback on claim-level certainty.
    - **Tone vs. Truth Gauge**: Comparison of stylistic persuasion vs. clinical evidence.
    - **Meaningful Friction**: Slow-down mechanisms like analysis cooldowns and verification gates.
    - **Human Accountability reminders**: Context-aware prompts for professional sign-off.

### **Analytics & Logging Pipeline**
- **Analytics**: Tracks "Trust Calibration" metrics (how often users verify vs. trust).
- **Logging**: A "Verification Ledger" providing an audit trail for all professional sign-offs.

### **Scheduler & Maintenance Layer**
- **Location**: `scheduler/`
- **Function**: Background maintenance for system-wide heuristics and thresholds.
- **Responsibilities**:
    - **Heuristic Refinement**: Updates keyword mappings for intent classification.
    - **Threshold Calibration**: Adjusts confidence requirements based on verification rates.
    - **Pattern Sync**: Updates bias and hallucination tracking markers.
- **Automation**: Triggered daily via GitHub Actions at 10 AM UTC.

---

## 5. Phase 5 Implementation Details
- `certification_service.py`: Logic for generating "Certified Output" summaries.
- `feedback_service.py`: Handles hallucination reporting and user feedback loops.
- `history_tracker.py`: Tracks temporal trends in verification and confidence calibration.

---

## 5. Folder Structure
```text
/
├── data/research/          # Analyzed survey, interview, and synthesis data
├── phase1_research/        # Strategy, PRD, MVP Scope, and Analysis frameworks
├── phase2_api/             # Groq and LLM provider integration layers
├── phase3_backend/         # FastAPI, Orchestration, and Database logic
├── phase4_frontend/        # Next.js, UI Components, and State management
├── phase5_verification/    # Source Auditor, Search APIs, and Fact-check logic
├── scheduler/              # Background tasks and periodic audit services
├── shared/                 # Config, .env, and shared utilities
├── docs/                   # Technical documentation and architecture
├── tests/                  # Unit, Integration, and E2E tests
├── README.md               # Project overview
└── architecture.md         # Detailed system design
```

---

## 6. Human Accountability Framework
The system is built on the principle that the **User is the Final Decision Maker (FDM)**. 
- **Decision Sign-offs**: Mandatory for high-stakes reports.
- **Evidence Bench**: Users must "pin" evidence to claims before finalization.
- **Accountability Ledger**: Tracking human verification steps for professional auditing.
