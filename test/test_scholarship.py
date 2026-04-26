from agent.tools.scholarship_tools import find_scholarships

profile = {
    "level": "bachelor",
    "field": "computer science",
    "country_preference": "canada"
}

res = find_scholarships.invoke(profile)

print("Results:", res[:2])
