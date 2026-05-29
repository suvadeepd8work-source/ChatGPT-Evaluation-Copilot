# Frontend Documentation - Phase 4 Prototype

## Overview
The Phase 4 frontend is a high-fidelity React prototype of the "ChatGPT Evaluation Mode". It focuses on "Evidence-Based UI" and "Meaningful Friction" to promote human accountability.

## Tech Stack
- **Framework**: React 18 (Vite)
- **Styling**: Tailwind CSS
- **Icons**: Lucide React
- **State Management**: Zustand
- **Animations**: Framer Motion

## Key UI Components
### 1. Evaluation Toggle
Located in the chat header, this allows users to switch between "Standard" mode and "Evaluation" mode. Evaluation mode triggers the **Evidence Bench**.

### 2. Evidence Bench (`EvaluationPane.tsx`)
A dedicated side panel that appears in Evaluation Mode to decompose and analyze the AI response.

#### **Sub-components**:
- **Confidence Indicator**: Visualizes the hybrid confidence score with detailed reasoning.
- **Tone vs Truth Gauge**: Measures the clinical/factual nature of the response vs its persuasive tone.
- **Bias Alerts**: Highlights persuasive patterns and provides de-biasing recommendations.
- **Claims Decomposition**: Breaks the response into atomic, verifiable claims that the user can interact with.
- **Verification Workflow**: A step-by-step checklist for the user to perform manual audits.
- **Accountability Reminders**: Dynamic warnings that escalate based on stake level.

### 3. Meaningful Friction
The prototype implements "Useful Friction" to slow down human decision-making:
- **Analysis Lock**: A mandatory cooldown period (3-10s) before a decision can be finalized.
- **Verification Gate**: In high-stakes scenarios, the "Confirm" button is disabled until the user manually checks all claims in the Evidence Bench.

## State Management
The `evaluationStore` manages the active evaluation data, the state of verified claims, and the loading/mode toggles.

## Design Aesthetic
The UI follows an **OpenAI-inspired aesthetic**:
- Dark mode by default (`#212121`).
- Minimalist typography.
- Subtle glassmorphism and backdrop blurs.
- Green (`#10a37f`) for primary actions, but introducing a critical Evaluation Green (`#10a37f`) and Warning Yellow/Red for risk-aware states.
