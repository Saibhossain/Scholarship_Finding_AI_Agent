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

    # Nodes
    g.add_node("extract", extract_node)
    g.add_node("profile", profile_node)
    g.add_node("missing", missing_node)
    g.add_node("router", router_node)
    g.add_node("search", scholarship_node)
    g.add_node("essay", essay_node)
    g.add_node("tracker", tracker_node)

    # Entry
    g.set_entry_point("extract")

    # Core flow
    g.add_edge("extract", "profile")
    g.add_edge("profile", "missing")

    # 🔹 Missing info check
    g.add_conditional_edges(
        "missing",
        lambda s: s["action"],
        {
            "wait": END,         # ask user → stop
            "continue": "router" # go to decision
        }
    )

    # 🔹 Router decision
    g.add_conditional_edges(
        "router",
        lambda s: s["action"],
        {
            "search": "search",
            "essay": "essay",
            "profile": END  # fallback
        }
    )

    # 🔹 Search flow
    g.add_edge("search", "tracker")

    # 🔹 Essay flow
    g.add_edge("essay", "tracker")

    # End
    g.add_edge("tracker", END)

    return g.compile(checkpointer=get_memory())
