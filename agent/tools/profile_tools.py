from langchain.tools import tool
from agent.db.database import SessionLocal
from agent.db.crud import update_profile, get_or_create_profile

def _update_profile_internal(session_id: str, data: dict):
    db = SessionLocal()
    profile = update_profile(db, session_id, data)
    db.close()
    return profile


def _get_profile_internal(session_id: str):
    db = SessionLocal()
    profile = get_or_create_profile(db, session_id)
    db.close()
    return profile


@tool
def add_to_profile(data: dict):
    """
    Add or update user profile fields.
    """
    return data  # LLM only returns structured data
