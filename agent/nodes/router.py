def router_node(state):
    text = state["input"].lower()

    if "essay" in text:
        return {"action": "essay"}
    elif "scholarship" in text:
        return {"action": "search"}
    else:
        return {"action": "profile"}
