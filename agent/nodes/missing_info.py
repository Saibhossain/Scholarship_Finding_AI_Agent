REQUIRED = ["level", "gpa", "field", "country_preference"]

def missing_node(state):
    profile = state.get("profile", {})
    missing = [f for f in REQUIRED if not profile.get(f)]

    if missing:
        return {"result": f"Missing: {missing}", "action": "wait"}

    return {"action": "continue"}
