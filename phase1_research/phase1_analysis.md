# Phase 1: Deep Analysis & Framework Design

## 1. Research Analysis Recap
The foundational research (Survey, Personas, Interviews) reveals a **"Fluency vs. Veracity" gap**. Users consistently misinterpret a model's confident tone as factual accuracy. 
- **Core Finding**: Verification is currently "Reactive" (only when something looks wrong) rather than "Proactive" (built into the workflow).
- **Target Barrier**: Automation Bias—the tendency to favor suggestions from automated systems even when they contradict human reasoning.

---

## 2. Intent Taxonomy
To calibrate evaluation, the system must first understand *why* the user is interacting with the AI.

| Intent Category | Examples | Risk Level | Evaluation Focus |
| :--- | :--- | :--- | :--- |
| **Generative/Creative** | Brainstorming, drafting poems, social media ideas | **Low** | Style, tone, and inspiration. |
| **Synthesis/Summary** | Summarizing a PDF, condensing meeting notes | **Medium** | Completeness (was anything key missed?) and Neutrality. |
| **Logical/Technical** | Coding assistance, math problems, architectural advice | **High** | Verifiability (does it run?) and Edge-case handling. |
| **Factual/Critical** | Researching history, tax law, medical symptoms | **Critical** | Source existence, date accuracy, and cross-referencing. |

---

## 3. Trust Behavior Analysis
Based on user interviews, trust is driven by three main heuristics:
1. **The Fluency Heuristic**: "It sounds professional, so it must be right." (Seen in Riya's persona).
2. **The Consensus Heuristic**: "It aligns with what I already know, so I trust the rest." (Seen in Soumya's interview).
3. **The Efficiency Heuristic**: "I don't have time to check, and it hasn't failed me yet." (Seen in Arjun's persona).

**Evaluation Mode Objective**: Break these heuristics by introducing "Meaningful Friction."

---

## 4. Skepticism Calibration Framework
The goal is not to make the user distrust *everything*, but to help them find the "Optimal Skepticism Zone."

- **The Skepticism Dial**:
    - **Level 1 (Assisted)**: For low-risk tasks. The system highlights facts but doesn't block progress.
    - **Level 2 (Active)**: For medium-risk tasks. The system prompts the user: "This summary omitted 20% of the source text. Review missing points?"
    - **Level 3 (Adversarial)**: For high-stakes tasks. The system hides the AI's "Confident" wording and forces the user to verify each claim against an external source before the "Copy" button is enabled.

---

## 5. Human Accountability Framework
The user must remain the **"Final Decision Maker" (FDM)**.

- **Decision Sign-off**: Every high-stakes response requires an explicit "Sign-off" from the user, acknowledging they have reviewed specific sections.
- **The Responsibility Log**: A record of *what* was verified, *how* it was verified, and *by whom*. This prevents "Responsibility Shifting" to the AI.
- **Evidence Benchmarking**: Users are encouraged (or required) to link an external source for any claim they mark as "Verified."

---

## 6. Evaluation Mode Requirements (System Level)
1. **Intent Classifier**: An NLP-based pre-processor that detects the user's intent category and sets the corresponding Skepticism Level.
2. **De-biasing Renderer**: A view that removes authoritative language (e.g., "Certainly!", "It is a fact that...") and presents data in a dry, neutral format.
3. **Verification Nudges**: Contextual UI popups that appear when the AI makes a high-confidence factual claim (dates, names, statistics).
4. **Source Auditor API**: A backend service that performs "shallow" verification (Does the URL exist?) and "deep" verification (Does the URL content match the claim?).
5. **Evaluation Dashboard**: A summary view for the user showing their "Verification Health" across their history.
