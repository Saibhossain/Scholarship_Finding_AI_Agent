from agent.db.database import SessionLocal
from agent.db.crud import save_essay
from agent.tools.essay_tools import evaluate_essay

def tracker_node(state):
    result = state.get("result", "")

    if isinstance(result, str) and len(result) > 200:
        feedback = evaluate_essay.invoke(result)

        db = SessionLocal()
        save_essay(db, state["session_id"], result, feedback)
        db.close()

        return {"result": result + "\n\n" + feedback}

    return state
