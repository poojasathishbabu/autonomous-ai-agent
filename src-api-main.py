from fastapi import FastAPI
from src_agent_main import *
app=FastAPI(title="Autonomous AI Agent API")
@app.get("/health")
def h(): return {"status":"ok"}
@app.post("/v1/agent/run")
def run(payload: dict):
    q=payload.get("query","")
    return {"query":q,"answer":f"Agent answer for {q}","tools_used":["search","db_query"],"latency_ms":210}
