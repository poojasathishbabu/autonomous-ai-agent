from src_agent_graph import plan_node, select_tool_node, execute_node, answer_node
import argparse
if __name__=="__main__":
    ap=argparse.ArgumentParser(); ap.add_argument("--query",default="Find Q3 revenue"); a=ap.parse_args()
    s={"query":a.query,"plan":[],"tool_calls":[],"context":"","answer":""}
    for fn in [plan_node, select_tool_node, execute_node, answer_node]: s.update(fn(s))
    print(s["answer"])
