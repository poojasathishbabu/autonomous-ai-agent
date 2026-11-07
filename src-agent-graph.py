"""LangGraph StateGraph: plan -> select_tool -> execute -> retrieve -> reflect -> answer"""
from typing import TypedDict, List
class State(TypedDict):
    query: str; plan: List[str]; tool_calls: List[dict]; context: str; answer: str
def plan_node(s: State): return {"plan": ["search","retrieve_db","answer"]}
def select_tool_node(s: State):
    q=s["query"].lower()
    if "revenue" in q or "database" in q: return {"tool_calls":[{"tool":"db_query","args":{"q":q}}]}
    return {"tool_calls":[{"tool":"search","args":{"q":q}}]}
def execute_node(s: State): return {"context": f"Tool result for {s['tool_calls']}"}
def answer_node(s: State): return {"answer": f"Answer to '{s['query']}' using context: {s.get('context','')}"}
# In production: from langgraph.graph import StateGraph; graph = StateGraph(State); graph.add_node...
if __name__=="__main__":
    s={"query":"Find Q3 revenue","plan":[],"tool_calls":[],"context":"","answer":""}
    s.update(plan_node(s)); s.update(select_tool_node(s)); s.update(execute_node(s)); s.update(answer_node(s)); print(s["answer"])
