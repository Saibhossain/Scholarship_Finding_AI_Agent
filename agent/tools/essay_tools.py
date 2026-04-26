from langchain.tools import tool
from agent.config import get_llm
from agent.prompts.system_prompts import ESSAY_PROMPT, EVALUATION_PROMPT

llm = get_llm()


@tool
def write_essay(profile: dict, scholarship: dict):
    """
    Generate a highly personalized scholarship essay.
    """

    # Extract meaningful fields (avoid dumping raw dict blindly)
    structured_profile = f"""
    Name: {profile.get('name')}
    Field: {profile.get('field')}
    GPA: {profile.get('gpa')}
    Level: {profile.get('level')}
    Country Preference: {profile.get('country_preference')}
    English Test: {profile.get('english_test')}
    """

    structured_scholarship = f"""
    Name: {scholarship.get('name')}
    Description: {scholarship.get('description')}
    Eligibility: {scholarship.get('eligibility')}
    Benefits: {scholarship.get('benefits')}
    """

    prompt = ESSAY_PROMPT.format(
        profile=structured_profile,
        scholarship=structured_scholarship
    )

    response = llm.invoke(prompt).content

    return response

@tool
def evaluate_essay(essay: str):
    """
    Evaluate essay quality and provide feedback.
    """

    response = llm.invoke(
        EVALUATION_PROMPT + f"\n\nEssay:\n{essay}"
    ).content

    return response
