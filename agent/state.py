from typing import TypedDict, Optional, Dict, Any

class AgentState(TypedDict):
    input: str
    action: Optional[str]
    profile: Dict[str, Any]
    result: Optional[Any]
