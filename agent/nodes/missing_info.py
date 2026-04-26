from agent.config import get_llm
from agent.db.database import SessionLocal
from agent.db.crud import update_profile
from agent.db.utils import serialize_sqlalchemy

llm = get_llm()

REQUIRED = ["level", "gpa", "field", "country_preference"]


def missing_node(state):
    session_id = state["session_id"]
    profile = state.get("profile", {})
    user_input = state.get("input", "")

    # 🔍 Step 1: Detect missing fields
    missing = [f for f in REQUIRED if not profile.get(f)]

    if not missing:
        return {"action": "continue"}

    # 🤖 Step 2: Try LLM inference from user input
    try:
        inference = llm.invoke(f"""
        Extract ONLY these missing fields from the user input if possible:
        {missing}

        Input:
        {user_input}

        Return JSON only.
        """).content

        import json
        inferred_data = json.loads(inference)

    except:
        inferred_data = {}

    # 🧠 Step 3: If we inferred something → update DB
    if inferred_data:
        db = SessionLocal()
        updated_profile = update_profile(db, session_id, inferred_data)
        db.close()

        clean_profile = serialize_sqlalchemy(updated_profile)

        # Re-check missing
        new_missing = [f for f in REQUIRED if not clean_profile.get(f)]

        if not new_missing:
            return {
                "profile": clean_profile,
                "action": "continue"
            }

        missing = new_missing
        profile = clean_profile

    # 💬 Step 4: Ask user (production-grade message)
    question_map = {
        "gpa": "What is your GPA (approximate is fine)?",
        "field": "What is your field of study?",
        "level": "What level are you studying (Bachelor/Master/PhD)?",
        "country_preference": "Which country do you want to study in?"
    }

    questions = [question_map.get(f, f"Please provide {f}") for f in missing]

    return {
        "result": {
            "type": "missing_info",
            "missing_fields": missing,
            "questions": questions,
            "message": "I need a bit more information to find the best scholarships for you."
        },
        "action": "wait"
    }
