from langchain.tools import tool

from agent.db.database import SessionLocal
from agent.db.crud import update_profile, get_or_create_profile

@tool
def add_to_profile(data: dict, session_id: str):
    """this tools is used to add user profile to database"""
    db = SessionLocal()
    profile = update_profile(db, session_id, data)
    db.close()

    return profile.__dict__

@tool
def get_profile(session_id: str):
    """ tools to used to get user profile """
    db = SessionLocal()
    profile = get_or_create_profile(db, session_id)
    db.close()

    return profile.__dict__

