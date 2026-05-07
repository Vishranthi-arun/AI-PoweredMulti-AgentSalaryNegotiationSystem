from crewai import Agent
from config.llm_config import get_llm

def get_mediator_agent():
    return Agent(
        role="Mediator",
        goal="Reach a fair agreement",
        backstory="Neutral negotiator balancing both sides.",
        verbose=True,
        llm=get_llm()
    )