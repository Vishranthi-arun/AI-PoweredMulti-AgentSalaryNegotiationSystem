from services.negotiation_services import run_negotiation

if __name__ == "__main__":
    result = run_negotiation(
        role="AI Engineer",
        experience=2,
        company='Google'
    )

    print("\nFINAL OUTPUT:\n")
    print(result)

