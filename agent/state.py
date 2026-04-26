from typing import TypedDict, Optional, Dict, Any

class AgentState(TypedDict):
    input: str
    session_id: str
    extracted_data: Optional[Dict[str, Any]]
    profile: Optional[Dict[str, Any]]
    action: Optional[str]
    result: Optional[Any]
