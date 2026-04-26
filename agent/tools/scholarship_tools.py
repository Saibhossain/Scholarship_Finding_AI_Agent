import requests
import os
from langchain.tools import tool

@tool
def find_scholarships(profile: dict):
    """
    Search scholarships based on user profile including level, field, and country preference.
    Returns a list of relevant scholarships.
    """
    
    url = "https://api.scholarshipapi.com/v1/scholarships"

    headers = {
        "X-API-Key": os.getenv("SCHOLARSHIP_API_KEY")
    }

    params = {
        "level": profile.get("level"),
        "field": profile.get("field"),
        "country": profile.get("country_preference")
    }

    res = requests.get(url, headers=headers, params=params)

    return res.json()

# @tool
# def find_scholarships(profile: dict):
#     """
#     Search scholarships based on user profile including level, field, and country preference.
#     Returns a list of relevant scholarships.
#     """
    
#     import requests, os

#     res = requests.get(
#         "https://api.scholarshipapi.com/v1/scholarships",
#         headers={"X-API-Key": os.getenv("SCHOLARSHIP_API_KEY")},
#         params=profile
#     )

#     return res.json()
