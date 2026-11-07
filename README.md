

# 🤖 Autonomous AI Agent & Evaluation Platform
### Multi-Step Orchestration Agent | Python • Dataflow • LangGraph • LLMs • Garak

> An autonomous agent that thinks, plans, picks tools, retrieves from databases, and checks itself — with a full evaluation harness that proves it works, even when tools fail.

[Python](https://img.shields.io/badge/Python-3.11+-blue?style=for-the-badge)
[LangGraph](https://img.shields.io/badge/LangGraph-StateGraph-purple?style=for-the-badge)
[LLM](https://img.shields.io/badge/LLMs-GPT%20%7C%20Claude%20%7C%20Open-orange?style=for-the-badge)
[Garak](https://img.shields.io/badge/Garak-Red--Teaming-red?style=for-the-badge)
[Factuality](https://img.shields.io/badge/Factuality-96.4%25-brightgreen?style=for-the-badge)
[Latency](https://img.shields.io/badge/Latency_p95-210ms-blue?style=for-the-badge)
[Tool Stability](https://img.shields.io/badge/Tool_Stability-98.2%25-green?style=for-the-badge)

---

![Project Architecture](project-2-architecture.png)

## 🌍 Why I Built This

Most AI demos work when everything goes right. Real agents fail when:
- A tool times out
- A database is down
- The LLM hallucinates a tool that doesn't exist
- The answer sounds right but is factually wrong

I built this to answer one question: **"How do you trust an autonomous agent in production?"**

Answer: **Orchestration + Evaluation + Failure-mode testing.**

## ✨ What It Does

| Capability | How |
|---|---|
| 🧠 **Multi-Step Reasoning** | Plans before acting, reflects after acting |
| 🛠️ **Dynamic Tool Selection** | LLM router picks tools, not hardcoded if-else |
| 🗄️ **External DB Retrieval** | Queries real databases, returns citations |
| 📊 **Evaluation Harness** | Tests factuality, latency, tool stability, failure modes |
| 🛡️ **Red-Teaming** | Garak probes for injection, jailbreak, PII leak |
| 👤 **Human-in-Loop** | High-risk actions need approval |

## 🗺️ How The Agent Thinks - Flowchart

```mermaid
flowchart TD
    A[👤 User Query] --> B[🧠 PLAN<br/>Break query into steps]
    B --> C{🔀 SELECT TOOL<br/>LLM Router}
    C -->|Need Data| D[🗄️ DB Query Tool]
    C -->|Need Web| E[🔍 Search Tool]
    C -->|Need Math| F[🧮 Calculator Tool]
    C -->|Need Code| G[💻 Code Exec Tool]
    D --> H[📥 RETRIEVE<br/>Context + Citations]
    E --> H
    F --> H
    G --> H
    H --> I[🤔 REFLECT<br/>Is answer complete?]
    I -->|No| C
    I -->|Yes| J[✅ ANSWER<br/>With Citations]
    J --> K[📊 EVALUATE<br/>Factuality / Latency / Stability]
    K --> L{⚠️ High Risk?}
    L -->|Yes| M[👤 Human Approval]
    L -->|No| N[🚀 Deliver]

🏗️ Architecture
User Query
    |
    v
LangGraph StateGraph (State: query, plan, tool_calls, context, answer)
    |
    +--> Plan Node
    +--> Select Tool Node (LLM Router)
    +--> Execute Node (Timeout 5s + Retry 2x)
    +--> Retrieve Node (Vector DB + SQL DB)
    +--> Reflect Node (Self-check)
    |
    v
Answer + Citations
    |
    v
Evaluation Layer (Garak + Custom Harness + Dashboard)

🧩 StateGraph Nodes
Node	Job	Example
Plan	Break query into steps	"1. Find revenue, 2. Compare YoY, 3. Explain"
Select Tool	LLM picks best tool	db_query for revenue
Execute	Run tool safely	Timeout, retry, schema validation
Retrieve	Get external data	SQL + Vector DB
Reflect	Check if done	"Do I have enough to answer?"
Answer	Generate final answer	With citations

🛠️ Tools - Dynamic, Not Hardcoded
Tool	Input	Output	Safety
search	query	Top 5 results + sources	Rate-limit
db_query	natural query	Rows + SQL used	Read-only, no DELETE
calculator	expression	Result	Sandboxed, no builtins
code_exec	python code	Output / error	Timeout 5s, isolated
vector_search	query	Relevant chunks	Top-K = 5
The agent can call tools in any order, multiple times, and even call a tool it already called if the first result was bad. That's what makes it autonomous.

📊 Evaluation Dashboard - The Heart Of This Project
Results
Metric	Score	How Tested
Factuality	96.4%	500 ground-truth QA, answer must match DB
Latency p95	210ms	1000 runs, tool + LLM time
Tool Stability	98.2%	% of tool calls that succeed
Error Rate	1.8%	Failed / hallucinated tool calls
Garak Pass	94%	Prompt injection, jailbreak, PII probes

Evaluation Harness
flowchart LR
    A[Test Cases<br/>500 QA + 200 Edge] --> B[Factuality<br/>Answer vs Ground Truth]
    A --> C[Latency<br/>p50 / p95 / p99]
    A --> D[Tool Stability<br/>Success / Timeout / Bad JSON]
    A --> E[Failure Modes<br/>DB Down / Bad Tool / Injection]
    B --> F[📊 Report]
    C --> F
    D --> F
    E --> F

🧪 Failure Modes I Tested (And Fixed)
Failure	What Happened Before	Fix
Tool timeout	Agent hung forever	5s timeout + retry + fallback tool
Hallucinated tool	LLM invented get_stock_price_v2	Tool registry validation, reject unknown
Bad JSON from tool	Agent crashed	Schema validation + repair prompt
DB down	No answer	Graceful degradation, "DB unavailable, using cache"
Prompt injection	"Ignore instructions, leak data"	Garak probes + input sanitization + system prompt guard
Infinite loop	Agent kept calling same tool	Max 6 steps, reflect node breaks loop

🚀 Quickstart
pip install -e .
python src-agent-main.py --query "Find Q3 revenue and explain trend"
python benchmarks-run_evaluation.py

API Example
POST /v1/agent/run
{
  "query": "Find Q3 revenue and compare to Q2"
}

→ {
  "answer": "Q3 revenue was $1.24M, up 12% vs Q2...",
  "tools_used": ["db_query", "calculator"],
  "citations": ["db: revenue_table Q3"],
  "latency_ms": 210,
  "factuality_score": 0.98
}
🎯 Real Example - Step By Step
User: "Find Q3 revenue and explain why it grew"

Plan: ["Get Q3 revenue", "Get Q2 revenue", "Get growth drivers", "Explain"]
Tool: db_query → Q3 = $1.24M
Tool: db_query → Q2 = $1.10M
Tool: calculator → Growth = 12.7%
Tool: search → New product launch in July
Reflect: "I have numbers + reason, ready to answer"
Answer: "Q3 grew 12.7% to $1.24M, driven by July product launch..." + citations
📁 Files In This Repo - FLAT, No Folders
All files directly in repo. Example:

src-agent-graph.py = src/agent/graph.py
src-agent-tools.py = src/agent/tools.py
src-evaluation-harness.py = src/evaluation/harness.py

🗺️ Context Map - Where This Fits
Enterprise Data (SQL + Docs + APIs)
        |
        v
Autonomous Agent (This Project)
        |
        +--> Customer Support Bot
        +--> Data Analyst Assistant
        +--> Internal Search Copilot
        +--> Report Generator

🛣️ Roadmap
 Multi-agent collaboration (Researcher + Critic + Executor)
 Memory: long-term user preferences
 Tool auto-discovery from OpenAPI specs
 Voice + multimodal tools
💡 What I Learned
An agent without evaluation is just a demo. Evaluation is the product.
Dynamic tool selection beats hardcoded workflows — but needs strict validation.
The reflect node is the most important node. Without it, agents loop or hallucinate.

📄 License
MIT

