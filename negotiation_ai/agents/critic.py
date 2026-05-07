from crewai import Agent
from config.llm_config import get_llm

def get_critic_agent():
    return Agent(
        role="Critic",
        goal="Evaluate fairness of the decision",
        backstory="Ensures outcomes are logical and realistic.",
        verbose=True,
        llm=get_llm(),
    )