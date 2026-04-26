import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

def get_llm():
    provider = os.getenv("LLM_PROVIDER", "openai").lower()

    # 🔵 OpenAI
    if provider == "openai":
        key = os.getenv("OPENAI_API_KEY")

        if not key or "your-openai" in key:
            raise ValueError("❌ Invalid OpenAI API key.")

        return ChatOpenAI(
            model="gpt-4o-mini",
            temperature=0.3,
            api_key=key
        )

    # 🟡 Gemini
    elif provider == "gemini":
        key = os.getenv("GEMINI_API_KEY")

        if not key:
            raise ValueError("❌ Missing Gemini API key.")

        return ChatGoogleGenerativeAI(
            model="gemini-2.5-flash",
            temperature=0.3,
            google_api_key=key
        )

    else:
        raise ValueError(f"❌ Unsupported LLM_PROVIDER: {provider}")
