from sqlalchemy.orm import Session
from agent.db.models import UserProfile, Essay

def get_or_create_profile(db: Session, session_id: str):
    profile = db.query(UserProfile).filter_by(session_id=session_id).first()

    if not profile:
        profile = UserProfile(session_id=session_id)
        db.add(profile)
        db.commit()
        db.refresh(profile)

    return profile


def update_profile(db: Session, session_id: str, data: dict):
    profile = get_or_create_profile(db, session_id)

    for key, value in data.items():
        setattr(profile, key, value)

    db.commit()
    db.refresh(profile)

    return profile


def save_essay(db: Session, session_id: str, content: str, feedback: str):
    essay = Essay(
        session_id=session_id,
        content=content,
        feedback=feedback
    )
    db.add(essay)
    db.commit()
