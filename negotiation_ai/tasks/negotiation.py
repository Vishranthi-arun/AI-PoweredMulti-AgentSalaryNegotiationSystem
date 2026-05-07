from crewai import Task

def create_tasks(agents, role, experience, company):

    market_task = Task(
        description=(
            f"You are a Market Analyst.\n"
            f"Find the latest salary trends for {role} with {experience} years experience.\n\n"
            f"Use available tools to fetch real-world salary data.\n"
            f"Consider industry demand, experience level, and skills.\n"
            f"Provide accurate and realistic salary benchmarks."
        ),
        expected_output=(
            "A detailed salary report including:\n"
            "- Minimum salary\n"
            "- Average salary\n"
            "- Maximum salary\n"
            "- Explanation based on current market trends\n"
            "- Mention if tool data was used"
        ),
        agent=agents["market"]
    )

    candidate_task = Task(
        description=(
            f"You are a candidate applying for {role} with {experience} years experience.\n\n"
            f"Review the market analysis and propose your expected salary.\n"
            f"Justify your expectation based on skills, experience, and demand.\n"
            f"Be confident and professional."
        ),
        expected_output=(
            "Candidate salary expectation including:\n"
            "- Expected salary\n"
            "- Justification\n"
            "- Professional tone"
        ),
        agent=agents["candidate"],
        context=[market_task]
    )

    recruiter_task = Task(
        description=(
            f"You are a recruiter hiring for {role}.\n\n"
            f"Review the candidate’s salary expectation.\n"
            f"Provide a counter offer considering company budget and market standards.\n"
            f"Ensure the offer is competitive but cost-effective."
        ),
        expected_output=(
            "Recruiter counter offer including:\n"
            "- Offered salary\n"
            "- Reasoning\n"
            "- Budget considerations"
        ),
        agent=agents["recruiter"],
        context=[candidate_task]
    )

    mediator_task = Task(
        description=(
            "You are a mediator resolving the salary negotiation.\n\n"
            "Analyze both candidate and recruiter perspectives.\n"
            "Suggest a fair and balanced final salary.\n"
            "Ensure both sides are reasonably satisfied."
        ),
        expected_output=(
            "Final salary agreement including:\n"
            "- Final salary\n"
            "- Justification\n"
            "- Explanation of compromise"
        ),
        agent=agents["mediator"],
        context=[candidate_task, recruiter_task]
    )

    critic_task = Task(
        description=(
            f"You are a critic evaluating the negotiation outcome for {company}.\n\n"
            f"Assess whether the final decision is fair, realistic, and justified.\n"
            f"Identify strengths and weaknesses.\n\n"
            f"IMPORTANT:\n"
            f"- Always refer to the company as '{company}'\n"
            f"- DO NOT use placeholders like [Company Name]\n"
        ),
        expected_output=(
            f"Evaluation report for {company} including:\n"
            f"- Fairness assessment\n"
            f"- Strengths\n"
            f"- Weaknesses\n"
            f"- Suggestions for improvement\n"
            f"- The company name '{company}' must appear in the response"
        ),
        agent=agents["critic"],
        context=[mediator_task]
    )

    return [market_task, candidate_task, recruiter_task, mediator_task, critic_task]