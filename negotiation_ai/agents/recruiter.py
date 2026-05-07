from crewai import Agent
from config.llm_config import get_llm

def get_recruiter_agent():
    return Agent(
        role="Recruiter",
        goal="Hire candidate at lowest possible cost",
        backstory="Represents company budget constraints.",
        verbose=True,
        llm=get_llm()
    )