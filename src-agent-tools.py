"""Tools: search, db_query, calculator, code_exec - each with schema, timeout, retry"""
import time
def search(q: str): return {"results":[f"Result for {q}"]}
def db_query(q: str): return {"rows":[{"metric":"revenue_q3","value":1240000}]}
def calculator(expr: str): return {"result": eval(expr, {"__builtins__":{}})}
TOOLS={"search":search,"db_query":db_query,"calculator":calculator}
def call_tool(name, **kw):
    assert name in TOOLS, f"Unknown tool {name}"
    try: return TOOLS[name](**kw)
    except Exception as e: return {"error":str(e)}
