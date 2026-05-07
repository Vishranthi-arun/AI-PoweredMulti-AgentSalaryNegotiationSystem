from crewai import Agent
from config.llm_config import get_llm

def get_candidate_agent():
    return Agent(
        role="Candidate",
        goal="Negotiate to maximize salary",
        backstory="A skilled professional aiming for the best compensation.",
        verbose=True,
        llm = get_llm()
    )