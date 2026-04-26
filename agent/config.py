import os
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI

load_dotenv()

def get_llm():
    return ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0.3,
        api_key=os.getenv("OPENAI_API_KEY")
    )
