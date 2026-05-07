from crewai import LLM

def get_llm():
    return LLM(
        model="ollama/mistral",
        base_url="http://localhost:11434"
    )
