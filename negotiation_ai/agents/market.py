from crewai import Agent
#from crewai_tools import SerperDevTool
from config.llm_config import get_llm
from tool.salary_tools import get_salary_data

#search_tool = SerperDevTool()

def get_market_agent():
    return Agent(
        role="Market Analyst",
        goal="Provide accurate salary insights using real-time data",
        backstory="Expert in job market trends and compensation analysis.",
        #tools=[search_tool],
        verbose=True,
        tools=[get_salary_data],
        llm=get_llm()
    )
