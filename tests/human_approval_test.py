from agents import Runner

from agent_modules.prioritisation_agent import (
    prioritisation_agent,
)


def main():

    print("\n--- TaskFlow Human Approval Test ---\n")

    result = Runner.run_sync(
        prioritisation_agent,
        """
        Prioritise TaskFlow's current feature candidates.

        After identifying the highest-priority feature,
        request human approval for that feature before
        proceeding.
        """
    )

    if result.interruptions:

        print("\n--- HUMAN APPROVAL REQUIRED ---\n")

        state = result.to_state()

        for interruption in result.interruptions:

            print(
                f"Approval requested for: "
                f"{interruption.name}"
            )

            decision = input(
                "\nApprove this product decision? "
                "(yes/no): "
            ).strip().lower()

            if decision in ["yes", "y"]:

                state.approve(interruption)

                print(
                    "\nDecision approved by Product Manager."
                )

            else:

                state.reject(interruption)

                print(
                    "\nDecision rejected by Product Manager."
                )

        print("\n--- Resuming Agent Workflow ---\n")

        result = Runner.run_sync(
            prioritisation_agent,
            state
        )

    print("\n--- Final Result ---\n")

    print(result.final_output)


if __name__ == "__main__":
    main()