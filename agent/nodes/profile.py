from langchain.chat_models import ChatOpenAI
import json

llm = ChatOpenAI(model="gpt-4o-mini")

def profile_node(state):
    text = state["input"]

    extraction = llm.invoke(f"""
    Extract structured JSON:

    {text}
    """).content

    try:
        data = json.loads(extraction)
    except:
        data = {}

    profile = state.get("profile", {})
    profile.update(data)

    return {"profile": profile}
