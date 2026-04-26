from agent.tools.essay_tools import write_essay, evaluate_essay
from dotenv import load_dotenv
load_dotenv()

profile = {
    "name": "Rokib",
    "field": "Computer Science",
    "gpa": 3.8,
    "level": "bachelor",
    "country_preference": "Canada"
}

scholarship = {
    "name": "Global Scholars Award",
    "description": "Supports international students in tech"
}

essay = write_essay.invoke({
    "profile": profile,
    "scholarship": scholarship
})

print("\n--- ESSAY ---\n", essay)

feedback = evaluate_essay.invoke(essay)

print("\n--- FEEDBACK ---\n", feedback)
