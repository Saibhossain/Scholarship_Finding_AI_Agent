import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

def get_llm():
    key = os.getenv("OPENAI_API_KEY")

    if not key or "your-openai" in key:
        raise ValueError("❌ Invalid OpenAI API key. Check your .env file.")

    return ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0.3,
        api_key=key
    )


print(os.getenv("OPENAI_API_KEY"))
