from agent.config import get_llm
llm =get_llm()

def router_node(state):
    text = state["input"]

    decision = llm.invoke(f"""
    Classify user intent:
    - search
    - essay
    - profile

    Input: {text}
    """).content.strip().lower()

    return {"action": decision}

