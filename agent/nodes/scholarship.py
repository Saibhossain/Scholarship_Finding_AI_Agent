from agent.tools.scholarship_tools import find_scholarships
from agent.tools.web_tools import search_web

def scholarship_node(state):
    profile = state["profile"]

    res = find_scholarships.invoke(profile)

    if not res:
        res = search_web.invoke("latest scholarships")

    return {"result": res}
