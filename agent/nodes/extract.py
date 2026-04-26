import json
from agent.config import get_llm
from agent.prompts.system_prompts import PROFILE_EXTRACTION_PROMPT

llm = get_llm()

def extract_node(state):
    res = llm.invoke(PROFILE_EXTRACTION_PROMPT + state["input"]).content
    try:
        data = json.loads(res)
    except:
        data = {}

    return {"extracted_data": data}
