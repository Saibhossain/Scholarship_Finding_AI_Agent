from agent.tools.essay_tools import write_essay

def essay_node(state):
    profile = state["profile"]
    essay = write_essay.invoke(profile)
    return {"result": essay}
