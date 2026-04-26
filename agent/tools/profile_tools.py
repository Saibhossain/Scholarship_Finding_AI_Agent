from langchain.tools import tool

@tool
def add_to_profile(data: dict, state: dict):
    profile = state.get("profile", {})
    profile.update(data)
    return {"profile": profile}


@tool
def get_profile(state: dict):
    return state.get("profile", {})


@tool
def delete_from_profile(fields: list, state: dict):
    profile = state.get("profile", {})
    for f in fields:
        profile.pop(f, None)
    return {"profile": profile}

