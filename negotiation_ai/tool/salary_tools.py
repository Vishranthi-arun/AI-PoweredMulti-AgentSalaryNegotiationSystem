from crewai.tools import tool

@tool("Salary Estimator Tool")
def get_salary_data(role: str, experience: int, location: str = "India") -> str:
    """
    Returns estimated salary range for a role based on experience and location.
    """

    if location.lower() == "india":
        if experience <= 2:
            return "₹6 LPA – ₹15 LPA"
        elif experience <= 5:
            return "₹12 LPA – ₹25 LPA"
        else:
            return "₹25 LPA+"
    else:
        if experience <= 2:
            return "$80,000 – $130,000"
        elif experience <= 5:
            return "$120,000 – $180,000"
        else:
            return "$180,000+"