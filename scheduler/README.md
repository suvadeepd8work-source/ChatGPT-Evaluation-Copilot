# Evaluation Scheduler

This directory contains the background tasks and maintenance logic for the ChatGPT Evaluation Mode.

## 📋 Responsibilities
The scheduler is responsible for the daily refinement of the system's critical analysis capabilities:

1.  **Daily Heuristic Updates**: Refines intent classification keywords and stake-detection logic based on user interaction trends.
2.  **Confidence Threshold Updates**: Dynamically adjusts confidence requirements for high-stakes vs. low-stakes queries.
3.  **Bias Detection Refresh**: Updates the patterns and stylistic markers used by the Bias Engine.
4.  **Hallucination Pattern Tracking**: Analyzes the `hallucination_reports` from Phase 5 to identify systemic weaknesses in specific LLM responses.
5.  **Research Insight Refresh**: Integrates new qualitative findings from ongoing user interviews and trust analysis.

## 🚀 Execution
The scheduler is automatically triggered via GitHub Actions:
- **Frequency**: Daily at 10:00 AM UTC.
- **Workflow**: `.github/workflows/scheduler.yml`.

## 🛠️ Manual Run
To run the scheduler locally for testing:
```bash
python scheduler/main.py
```
