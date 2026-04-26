from agent.db.database import SessionLocal
from agent.db.crud import update_profile
from agent.db.utils import serialize_sqlalchemy

def profile_node(state):
    db = SessionLocal()

    profile_obj = update_profile(
        db,
        state["session_id"],
        state.get("extracted_data", {})
    )

    db.close()

    profile = serialize_sqlalchemy(profile_obj)  

    return {"profile": profile}
