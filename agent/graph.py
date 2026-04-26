from langgraph.graph import StateGraph, END
from agent.state import AgentState
from agent.memory.memory import get_memory

from agent.nodes.router import router_node
from agent.nodes.extract import extract_node
from agent.nodes.profile import profile_node
from agent.nodes.missing_info import missing_node
from agent.nodes.scholarship import scholarship_node
from agent.nodes.essay import essay_node
from agent.nodes.tracker import tracker_node

def build_graph():
    g = StateGraph(AgentState)

    g.add_node("router", router_node)
    g.add_node("extract", extract_node)
    g.add_node("profile", profile_node)
    g.add_node("missing", missing_node)
    g.add_node("search", scholarship_node)
    g.add_node("essay", essay_node)
    g.add_node("tracker", tracker_node)

    g.set_entry_point("router")

    g.add_edge("router", "extract")
    g.add_edge("extract", "profile")
    g.add_edge("profile", "missing")

    g.add_conditional_edges(
        "missing",
        lambda s: s["action"],
        {"wait": END, "continue": "search"}
    )

    g.add_edge("search", "tracker")
    g.add_edge("essay", "tracker")
    g.add_edge("tracker", END)

    return g.compile(checkpointer=get_memory())
