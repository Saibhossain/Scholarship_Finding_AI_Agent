import requests
from langchain.tools import tool
import os
from dotenv import load_dotenv
load_dotenv()


@tool
def search_web(query: str):
    """
    Search the web for latest information such as scholarships, requirements, or opportunities.
    """

    url = "https://api.tavily.com/search"
    
    payload = {
        "api_key": os.getenv("TAVILY_API_KEY"),
        "query": query
    }

    res = requests.post(url, json=payload).json()

    # ✅ Clean results for LLM
    cleaned = [
        {
            "title": r["title"],
            "url": r["url"],
            "summary": r["content"]
        }
        for r in res.get("results", [])[:5]
    ]

    return cleaned