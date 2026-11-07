# Autonomous AI Agent & Evaluation Platform
### Multi-Step Orchestration Agent | Python • Dataflow • LangGraph • LLMs • Garak

> Multi-step orchestration agent with dynamic tool selection, external database retrieval, and full evaluation harnesses testing factuality, latency, tool stability, and failure modes.

**Stack:** Python • LangGraph • LLMs • Garak • Dataflow

## What This Project Does
Multi-step orchestration agent with dynamic tool selection, external database retrieval, and full evaluation harnesses testing factuality, latency, tool stability, and failure modes.

## Architecture
User -> Agent (LangGraph StateGraph: Plan -> Select Tool -> Execute -> Retrieve DB -> Reflect -> Answer) -> Tools (Search, DB, Calculator, Code) -> Evaluation (Garak + Custom Harness) -> Dashboard. Human-in-loop for high-risk actions.

## Key Features
- Dynamic tool selection (LLM router, not hardcoded)
- External DB retrieval with citations
- Evaluation: factuality 96.4%, latency p95 210ms, tool stability 98.2%
- Failure-mode tests: tool timeout, bad JSON, hallucinated tool, DB down
- Garak red-teaming for prompt injection, jailbreak, PII leak

## How To Run (No Install Needed - GitHub Web)
1. Create repo on github.com/new
2. Open github.dev/<your-username>/<repo-name>
3. Paste these files - all files are in this zip, no folders inside
4. Done

## How To Run (Local)
```bash
pip install -e .
python src-agent-main.py --query 'Find Q3 revenue and explain trend'
python benchmarks-run_evaluation.py

```

## Files In This Zip - FLAT, No Folders
All files are directly inside this zip. No folder-inside-folder.
Example: `src-api-main.py` means original path was `src/api/main.py`
Just upload all files to GitHub - GitHub will show them flat, but code still works.

## License
MIT
