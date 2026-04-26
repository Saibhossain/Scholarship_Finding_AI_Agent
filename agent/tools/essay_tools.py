from langchain.chat_models import ChatOpenAI
from langchain.tools import tool

llm = ChatOpenAI(model="gpt-4o-mini")

@tool
def write_essay(profile: dict, scholarship: dict):
    prompt = f"""
    Write a professional scholarship essay.

    Profile:
    {profile}

    Scholarship:
    {scholarship}

    400 words, compelling.
    """

    return llm.invoke(prompt).content


@tool
def evaluate_essay(essay: str):
    return llm.invoke(f"""
    Evaluate this essay (score 1-10 + feedback):

    {essay}
    """).content

