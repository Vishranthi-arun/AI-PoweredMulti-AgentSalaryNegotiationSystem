from agents.candidate import get_candidate_agent
from agents.recruiter import get_recruiter_agent
from agents.market import get_market_agent
from agents.mediator import get_mediator_agent
from agents.critic import get_critic_agent

def get_agents():
    return {
        "candidate": get_candidate_agent(),
        "recruiter": get_recruiter_agent(),
        "market": get_market_agent(),
        "mediator": get_mediator_agent(),
        "critic": get_critic_agent()
    }