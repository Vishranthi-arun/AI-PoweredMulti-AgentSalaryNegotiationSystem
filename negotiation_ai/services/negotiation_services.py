from crewai import Crew
from crew.crew_setup import get_agents
from tasks.negotiation import create_tasks

def run_negotiation(role, experience, company):
    agents = get_agents()
    tasks = create_tasks(agents, role, experience, company)

    crew = Crew(
        agents=list(agents.values()),
        tasks=tasks,
        verbose=False
    )

    result = crew.kickoff()

    return {
        "input": {
            "role": role,
            "experience": experience,
            "company": company
        },
        "output": str(result)
    }
