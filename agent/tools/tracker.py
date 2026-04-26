from langchain.tools import tool

from agent.db.database import SessionLocal
from agent.db.crud import save_essay
from agent.tools.essay_tools import evaluate_essay

@tool
def tracker_node(state):
    """ track essay record """
    session_id = state["session_id"]
    result = state.get("result", "")

    if len(result) > 200:
        feedback = evaluate_essay.invoke(result)

        db = SessionLocal()
        save_essay(db, session_id, result, feedback)
        db.close()

        return {
            "result": f"{result}\n\nFeedback:\n{feedback}"
        }

    return state
