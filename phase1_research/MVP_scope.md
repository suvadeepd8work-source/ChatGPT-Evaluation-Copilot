# MVP Scope: ChatGPT Evaluation Mode

## 1. Core Goal
Demonstrate the "Evaluation Mode" by implementing a functional pipeline for high-stakes research verification.

## 2. Included in MVP
- **Dual-Pane UI**: Basic chat interface with a sidebar for "Evidence Bench."
- **Source Auditor**: Real-time URL/DOI verification for extracted links.
- **Manual Sign-off**: A checkbox system for the user to "verify" key claims.
- **De-biasing Toggle**: A simple button to switch to "Clinical Text" mode.
- **Intent Classifier**: A basic rule-based classifier for detecting High-Stakes keywords (e.g., "Tax," "Medical," "Research").

## 3. Excluded from MVP (Post-MVP)
- **Multi-Agent Critiques**: (Requires higher latency and cost).
- **Historical Evaluation Dashboard**: (Focusing on the immediate interaction first).
- **Consensus Mode**: (Multi-user collaboration).
- **Automated "Adversarial" Prompts**: (Will be added in Phase 3).

## 4. Success Criteria for MVP
- User can highlight a claim and pin a verified URL to it in the sidebar.
- System successfully flags a "dead" or hallucinated URL provided by the AI.
- User is forced to wait 3 seconds before "Copying" a high-stakes response.
