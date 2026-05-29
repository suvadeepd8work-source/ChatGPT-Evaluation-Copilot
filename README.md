# ChatGPT Evaluation Mode

A specialized web application designed to transform AI interactions from "passive acceptance" to "critical evaluation." 

## 🌟 Philosophy
**AI is a collaborative assistant, not an authority.** 
In this application, the user is the final decision maker. The system's job is not just to provide answers, but to provide the tools and evidence necessary for the user to judge those answers critically.

## 🚀 Key Features
- **De-biasing UI**: Strip away the "persuasive" tone of AI to focus on raw facts.
- **FACT Framework**: Systematic evaluation of Factual Accuracy, Appropriateness, Completeness, and Truthfulness.
- **Source Auditor**: Real-time verification of citations and references to eliminate hallucinations.
- **Human-in-the-Loop Annotations**: Directly highlight and verify/refute AI claims.
- **Stake-Based Nudging**: Increased friction and verification requirements for high-stakes topics (Medical, Legal, Financial).

## 🛠️ Architecture Overview
The project is built on a multi-layered architecture focused on de-biasing, factual verification, and human accountability.

For more details, see [architecture.md](architecture.md).

## 📊 Research Basis
This project is built upon comprehensive research across multiple phases:

### **Data & Research Analysis**
- [Research Insights](data/research/research_insights.md): Summary of key findings from interviews and surveys.
- [Survey Analysis](data/research/survey_analysis.md): Quantitative data from 33+ user responses.
- [Interview Analysis](data/research/interview_analysis.md): Qualitative deep dive into user interviews.
- [Thematic Analysis](data/research/thematic_analysis.md): Analysis of recurring research themes.
- [Key Findings](data/research/key_findings.md): Core takeaways from the research phase.
- [Trust Analysis](data/research/trust_analysis.md): Deep dive into trust triggers and barriers.
- [Behavioral Patterns](data/research/behavioral_patterns.md): Analysis of overreliance and verification habits.
- [Evaluation Opportunities](data/research/evaluation_opportunities.md): Identifying high-risk scenarios.
- [Final Research Synthesis](data/research/final_research_synthesis.md): High-level synthesis of all research data.
- [Detailed Personas](data/research/detailed_personas.md): Expanded product personas (Riya, Arjun, Neha).

### **Phase 1: Strategy & Requirements**
- [Phase 1 Analysis](phase1_research/phase1_analysis.md): Deep dive into intent taxonomy and skepticism calibration.
- [Product Requirements (PRD)](phase1_research/product_requirements.md): Detailed functional and technical requirements.
- [Evaluation Mode Strategy](phase1_research/evaluation_mode_strategy.md): Strategic tiers for verification and HITL protocols.
- [MVP Scope](phase1_research/MVP_scope.md): Defining the first functional iteration.
- [Feature Prioritization](phase1_research/feature_prioritization.md): Data-driven roadmap for the application.
- [Product & UX Recommendations](phase1_research/recommendations.md): Strategic design recommendations.

### **Phase 5: Verification & Final Refinement**
- [Certification Service](phase5_verification/certification_service.py): Generation of "Certified Output" summaries.
- [Feedback Service](phase5_verification/feedback_service.py): Hallucination reporting and user feedback loops.
- [History Tracker](phase5_verification/history_tracker.py): Tracking verification progress and confidence trends.

## 🛠️ Local Setup

### **1. Prerequisites**
- Python 3.10+
- Node.js 18+
- [Groq API Key](https://console.groq.com/)

### **2. Environment Configuration**
Create a `.env` file in the root directory with the following variables:
```env
GROQ_API_KEY=your_groq_api_key_here
```

### **3. Backend Setup (FastAPI)**
Navigate to the backend directory and install dependencies:
```bash
cd phase3_backend
pip install -r requirements.txt
mkdir storage
```
Run the backend server:
```bash
python main.py
```
The API will be available at `http://localhost:8000`.

### **4. Frontend Setup (React + Vite)**
Navigate to the frontend directory and install dependencies:
```bash
cd phase4_frontend
npm install
```
Run the development server:
```bash
npm run dev
```
The application will be available at `http://localhost:5173`.

## 🚀 Deployment
The application uses a **Hybrid Deployment** strategy:
- **Frontend**: Deployed on [Vercel](https://vercel.com).
- **Backend**: Deployed on [Render](https://render.com).

For detailed production setup and environment configuration, see [deployment.md](deployment.md).

## 🔄 Development Workflow
1. **Intent Classification**: Every prompt is analyzed for stake levels (Low to Critical).
2. **AI Orchestration**: The backend calls Groq (Llama 3.3 70B) with specialized system prompts.
3. **Evaluation Engines**: Responses are passed through Confidence, Bias, and Tone engines.
4. **Verification**: Users can interact with the Evaluation Pane to verify claims and actions.
5. **Session Management**: Interactions are stored in a local SQLite database for persistence.

## 📄 License
TBD
