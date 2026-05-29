# Detailed Product Personas: ChatGPT Evaluation Mode

## 1. Riya: The Overtrusting Student
*“If it sounds professional, I trust it.”*

- **Background**: 21-year-old Undergraduate Student. Uses AI for assignments, lecture summaries, and explaining complex concepts.
- **Goals**: Finish homework quickly; simplify academic jargon; maintain a good GPA with minimal effort.
- **Frustrations**: Long research papers; complex technical language; feeling overwhelmed by information volume.
- **Trust Behavior**: **High/Blind Trust**. Equates professional formatting and authoritative tone with factual accuracy.
- **AI Dependency Level**: **High**. Relies on AI as her primary learning and writing assistant.
- **Evaluation Habits**: **Minimal**. Only checks if the output "looks" right or fits the assignment length.
- **Technical Expertise**: **Low**. Basic prompting; lacks knowledge of LLM hallucinations.
- **Risk Level**: **Medium**. Main risks are academic integrity issues and significant learning gaps.
- **Verification Tendencies**: **Very Low**. Rarely leaves the AI chat interface to verify facts.
- **Failure Scenario**: Submitting an essay containing hallucinated historical dates or fabricated scientific studies.

### **Persona Mapping**
| Category | Requirement |
| :--- | :--- |
| **Useful Features** | De-biasing UI, Intent-Adaptive Friction, Mandatory Pause, Simple Fact-check Nudges. |
| **Friction Mechanism** | **High Friction**: 5-second lock on "Copy" button for high-stakes topics; mandatory "Did you check this?" prompt. |
| **Confidence Threshold** | **90%**: Flag any claim with less than 90% confidence or missing citations. |

---

## 2. Arjun: The Cautious Professional
*“AI helps me work faster, but I still verify important outputs.”*

- **Background**: 27-year-old Marketing Associate. Uses AI for client reports, email drafts, and brainstorming campaign ideas.
- **Goals**: Increase productivity; improve writing style; generate creative content hooks.
- **Frustrations**: AI "echo-chambering" his own ideas; fear of sending misinformation to clients.
- **Trust Behavior**: **Moderate/Conditional**. Trusts for creative tasks but is skeptical of factual data.
- **AI Dependency Level**: **Moderate**. Uses AI as a productivity multiplier and brainstorming partner.
- **Evaluation Habits**: **Inconsistent**. Verifies when he knows the "stakes are high" (e.g., client-facing reports).
- **Technical Expertise**: **Medium**. Understands that AI can be wrong but doesn't always know *where* it's wrong.
- **Risk Level**: **High**. Professional reputation and brand integrity are at stake.
- **Verification Tendencies**: **Medium**. Cross-checks against manual reviews and known brand guidelines.
- **Failure Scenario**: Including a hallucinated competitor statistic in a high-profile marketing strategy deck.

### **Persona Mapping**
| Category | Requirement |
| :--- | :--- |
| **Useful Features** | Fact-to-Fluff Heatmap, Human Sign-off Workflow, Verification Nudges, Tone De-biaser. |
| **Friction Mechanism** | **Medium Friction**: Verification checklists required for "Professional Work" intent; "Confidence Heatmap" visible by default. |
| **Confidence Threshold** | **80%**: Highlight claims that lack strong external corroboration or high-probability reasoning. |

---

## 3. Neha: The Research-Focused User
*“I trust AI only when evidence is provided.”*

- **Background**: 24-year-old Research Intern. Uses AI for data analysis, literature reviews, and synthesizing research papers.
- **Goals**: Quickly identify key findings in large datasets; find relevant source material; audit AI logic.
- **Frustrations**: Fake citations (hallucinated DOIs/URLs); weak logical reasoning; lack of transparency.
- **Trust Behavior**: **Low/Skeptical**. Adopts an "Adversarial" mindset; treats AI as a fallible assistant.
- **AI Dependency Level**: **Low/Medium**. Uses AI for structural help and initial analysis, never for final facts.
- **Evaluation Habits**: **High/Rigorous**. Regularly cross-checks every claim against primary sources.
- **Technical Expertise**: **High**. Aware of LLM architecture limitations; skilled in multi-step verification prompts.
- **Risk Level**: **Very High**. Research integrity and scientific accuracy are paramount.
- **Verification Tendencies**: **Extremely High**. Always hunts for the source; uses "Logic Tree" to audit reasoning.
- **Failure Scenario**: Basing a research hypothesis on a "logical fallacy" or "subtle error" hidden in an AI-generated synthesis.

### **Persona Mapping**
| Category | Requirement |
| :--- | :--- |
| **Useful Features** | Source Auditor (DOI/URL check), Logic Tree Visualization, Evidence Bench, Citation Snippets. |
| **Friction Mechanism** | **Low Friction**: Focus on "Power Tools" rather than "Blocks." Provide an "Evidence Bench" to assist her existing workflow. |
| **Confidence Threshold** | **Variable/Low (70%)**: She wants to see *all* evidence, even low-confidence ones, so she can verify them herself. |
