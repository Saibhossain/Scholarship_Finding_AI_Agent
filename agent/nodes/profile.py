from agent.db.database import SessionLocal
from agent.db.crud import update_profile

def profile_node(state):
    db = SessionLocal()

    profile = update_profile(
        db,
        state["session_id"],
        state.get("extracted_data", {})
    )

    db.close()

    return {"profile": profile.__dict__}
