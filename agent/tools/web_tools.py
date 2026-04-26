import requests
from langchain.tools import tool
import os

@tool
def search_web(query: str):
    url = "https://api.tavily.com/search"
    
    payload = {
        "api_key": os.getenv("TAVILY_API_KEY"),
        "query": query
    }

    res = requests.post(url, json=payload)
    return res.json()
