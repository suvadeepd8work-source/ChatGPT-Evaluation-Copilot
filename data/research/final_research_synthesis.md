# Final Research Synthesis: ChatGPT Evaluation Mode

## 1. Core Product Direction
The "ChatGPT Evaluation Mode" is a **behavioral intervention system** designed to shift users from **Passive Acceptance** to **Active Interrogation**. It addresses the core research finding that professional-sounding AI fluency is the primary driver of unearned trust.

## 2. Most Critical Trust Problems
- **The Fluency Fallacy**: 100% of novice personas equate structural clarity and authoritative tone with accuracy.
- **Hidden Hallucinations**: Factual errors embedded in confident, well-formatted prose are rarely caught unless the user is already an expert.
- **Source Fabrication**: "Fake citations" (hallucinated DOIs, URLs, and book titles) are a major pain point for researchers.
- **Automation Bias**: A significant percentage of users (48.5%) admit to skipping reviews due to time pressure or perceived AI reliability.

## 3. High-Priority Evaluation Features
- **Real-Time Source Auditor**: Verifying the existence and content of citations.
- **Confidence Heatmap**: Visualizing AI uncertainty across a response.
- **De-biasing UI**: Stripping persuasive formatting to reveal raw claims.
- **Human Sign-Off Workflow**: Forcing accountability for high-stakes outputs.

## 4. Risk Mitigation Strategies
- **Intent-Based Friction**: Automatically increasing verification requirements for financial, medical, or academic queries.
- **Adversarial Nudging**: Prompting users to consider alternative viewpoints when AI agreement is suspiciously high.
- **The "Evidence Bench"**: Requiring users to pin external verification before finalizing high-stakes reports.

## 5. Human Accountability Principles
- **User as Final Decision Maker (FDM)**: The system never "auto-approves" a high-stakes claim.
- **Traceability**: Maintaining a log of *who* verified *what* and *how*.
- **No Responsibility Shifting**: Clear UI messaging that AI is a "Collaborative Assistant," not an "Authority."

## 6. UX Direction
- **Dual-Pane Interaction**: AI response on one side, Evaluation/Evidence tools on the other.
- **Meaningful Friction**: Intentional delays and checklists to break the "Copy-Paste" habit.
- **Visual Evidence**: Using color-coding (🟢/🟡/🔴) to signal source status at a glance.

## 7. Backend Evaluation Requirements
- **Multi-Agent Critiques**: Using a second LLM to audit the primary LLM's response.
- **Search & Academic API Integration**: Real-time cross-referencing against live web and academic databases.
- **Fact-to-Fluff Ratio Engine**: Calculating and displaying the density of verifiable facts vs. elaborative prose.
