from agents import Runner, SQLiteSession
from pydantic import BaseModel

from agent_modules.orchestrator_agent import orchestrator_agent
from utils.logger import logger


# ---------------------------------------------------------
# Persistent Session Memory
# ---------------------------------------------------------

session = SQLiteSession(
    "taskflow_product_manager",
    "taskflow_memory.db"
)


# ---------------------------------------------------------
# Clean Output Formatter
# ---------------------------------------------------------

def display_result(output):
    """
    Display agent outputs in a clean, readable format.
    Supports both normal text and Pydantic structured outputs.
    """

    if output is None:
        print("No final output was produced.")
        return

    # Normal text response
    if not isinstance(output, BaseModel):
        print(output)
        return

    data = output.model_dump()

    for key, value in data.items():

        title = key.replace("_", " ").title()

        print(f"\n{title}:")

        # Handle lists
        if isinstance(value, list):

            if not value:
                print("None")
                continue

            for index, item in enumerate(value, start=1):

                # List containing structured objects
                if isinstance(item, dict):

                    print(f"\n{index}.")

                    for sub_key, sub_value in item.items():

                        sub_title = (
                            sub_key
                            .replace("_", " ")
                            .title()
                        )

                        # Nested lists
                        if isinstance(sub_value, list):

                            print(f"   {sub_title}:")

                            for nested_item in sub_value:
                                print(f"   - {nested_item}")

                        else:

                            print(
                                f"   {sub_title}: "
                                f"{sub_value}"
                            )

                else:

                    print(f"- {item}")

        # Handle dictionaries
        elif isinstance(value, dict):

            for sub_key, sub_value in value.items():

                sub_title = (
                    sub_key
                    .replace("_", " ")
                    .title()
                )

                print(
                    f"{sub_title}: "
                    f"{sub_value}"
                )

        # Normal values
        else:

            print(value)


# ---------------------------------------------------------
# Human Approval Handler
# ---------------------------------------------------------

def handle_approvals(result):

    while result.interruptions:

        logger.info(
            "Human approval requested."
        )

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

                logger.info(
                    "Product decision approved by human."
                )

                print(
                    "\nDecision approved by Product Manager."
                )

            else:

                state.reject(interruption)

                logger.warning(
                    "Product decision rejected by human."
                )

                print(
                    "\nDecision rejected by Product Manager."
                )

        print("\n--- Resuming Agent Workflow ---\n")

        result = Runner.run_sync(
            orchestrator_agent,
            state,
            session=session
        )

    return result


# ---------------------------------------------------------
# Main Application
# ---------------------------------------------------------

def main():

    logger.info(
        "TaskFlow AI Product Manager started."
    )

    print("\n" + "=" * 60)
    print("TASKFLOW AI PRODUCT MANAGER")
    print("=" * 60)

    print("Persistent Memory : ENABLED")
    print("Human Approval    : ENABLED")
    print("RAG Retrieval     : ENABLED")
    print("Logging           : ENABLED")

    print("\nType 'exit' to quit.\n")

    while True:

        user_request = input(
            "What would you like the AI Product Manager to do?\n> "
        ).strip()

        # Exit application
        if user_request.lower() in ["exit", "quit"]:

            logger.info(
                "TaskFlow AI Product Manager closed."
            )

            print(
                "\nTaskFlow AI Product Manager closed."
            )

            break

        # Ignore blank input
        if not user_request:
            continue

        logger.info(
            f"User request received: {user_request}"
        )

        try:

            # Run orchestrator
            result = Runner.run_sync(
                orchestrator_agent,
                user_request,
                session=session
            )

            # Handle human approval if required
            result = handle_approvals(result)

            # -------------------------------------------------
            # Display clean result
            # -------------------------------------------------

            print("\n" + "-" * 60)
            print("RESULT")
            print("-" * 60)

            display_result(
                result.final_output
            )

            # Show which specialist handled request
            print("\n" + "-" * 60)
            print("AGENT USED")
            print("-" * 60)

            print(
                result.last_agent.name
            )

            logger.info(
                f"Request completed successfully. "
                f"Final agent: {result.last_agent.name}"
            )

            print("\n" + "=" * 60 + "\n")

        # -----------------------------------------------------
        # Error Handling
        # -----------------------------------------------------

        except Exception as error:

            error_text = str(error)

            logger.exception(
                f"Agent execution failed: {error_text}"
            )

            print("\n" + "-" * 60)
            print("ERROR")
            print("-" * 60)

            # Gemini quota / rate limit
            if (
                "429" in error_text
                or "RESOURCE_EXHAUSTED" in error_text
                or "quota" in error_text.lower()
            ):

                print(
                    "The AI model rate limit or quota "
                    "has been reached."
                )

                print(
                    "Please wait and try again later "
                    "or use another available model."
                )

                logger.warning(
                    "Gemini quota/rate limit encountered."
                )

            # Tavily API problem
            elif (
                "TAVILY" in error_text.upper()
                or "tavily" in error_text.lower()
            ):

                print(
                    "Competitor research service "
                    "is currently unavailable."
                )

                print(
                    "Please check the Tavily API "
                    "configuration or try again later."
                )

                logger.warning(
                    "Tavily competitor search error."
                )

            # Gemini key missing
            elif "GEMINI_API_KEY" in error_text:

                print(
                    "Gemini API configuration is missing."
                )

                logger.error(
                    "Gemini API key configuration error."
                )

            # Everything else
            else:

                print(
                    "An unexpected error occurred while "
                    "processing the request."
                )

                print(
                    "The detailed error has been recorded "
                    "in logs/taskflow.log."
                )

            print()


# ---------------------------------------------------------
# Application Entry Point
# ---------------------------------------------------------

if __name__ == "__main__":
    main()