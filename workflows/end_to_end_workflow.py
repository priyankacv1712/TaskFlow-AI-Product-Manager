from agents import Runner

from agent_modules.feedback_agent import feedback_agent
from agent_modules.analytics_agent import analytics_agent
from agent_modules.competitor_agent import competitor_agent
from agent_modules.prioritisation_agent import prioritisation_agent
from agent_modules.prd_agent import prd_agent
from agent_modules.sprint_agent import sprint_agent


def run_feedback_analysis():

    print("\n" + "=" * 70)
    print("STEP 1 — CUSTOMER FEEDBACK ANALYSIS")
    print("=" * 70)

    result = Runner.run_sync(
        feedback_agent,
        """
        Analyse the current TaskFlow customer feedback dataset.

        Identify:
        - major customer pain points
        - recurring themes
        - feature requests
        - sentiment
        - highest-priority customer problem
        """
    )

    analysis = result.final_output

    print(f"\nFeedback items analysed: {analysis.total_feedback_items}")
    print(f"Top issue: {analysis.top_priority_issue}")

    return analysis


def run_product_analytics(feedback_analysis):

    print("\n" + "=" * 70)
    print("STEP 2 — PRODUCT ANALYTICS")
    print("=" * 70)

    result = Runner.run_sync(
        analytics_agent,
        f"""
        Analyse TaskFlow's current product metrics.

        Customer feedback has already identified this major issue:

        {feedback_analysis.top_priority_issue}

        Use the product metrics tool and determine whether the
        available analytics support or contradict this concern.

        Identify:
        - adoption issues
        - retention issues
        - performance concerns
        - biggest product concern
        """
    )

    analysis = result.final_output

    print(
        f"\nBiggest analytics concern: "
        f"{analysis.biggest_product_concern}"
    )

    return analysis


def run_competitor_research(
    feedback_analysis,
    analytics_analysis
):

    print("\n" + "=" * 70)
    print("STEP 3 — COMPETITOR & MARKET RESEARCH")
    print("=" * 70)

    result = Runner.run_sync(
        competitor_agent,
        f"""
        Research the current project-management software market
        and identify relevant opportunities for TaskFlow.

        Existing internal evidence:

        Customer concern:
        {feedback_analysis.top_priority_issue}

        Product analytics concern:
        {analytics_analysis.biggest_product_concern}

        Compare major competitors including:
        - Asana
        - Trello
        - Monday.com
        - ClickUp

        Identify market trends and product opportunities that
        may be relevant to the problems TaskFlow is experiencing.
        """
    )

    analysis = result.final_output

    print(
        f"\nRecommended market opportunity: "
        f"{analysis.recommended_product_opportunity}"
    )

    return analysis


def run_prioritisation(
    feedback_analysis,
    analytics_analysis,
    competitor_analysis
):

    print("\n" + "=" * 70)
    print("STEP 4 — FEATURE PRIORITISATION")
    print("=" * 70)

    result = Runner.run_sync(
        prioritisation_agent,
        f"""
        Prioritise TaskFlow's current feature candidates.

        Use the prioritisation tool and its calculated RICE
        scores.

        Consider the following supporting evidence:

        CUSTOMER FEEDBACK:
        {feedback_analysis.top_priority_issue}

        PRODUCT ANALYTICS:
        {analytics_analysis.biggest_product_concern}

        MARKET OPPORTUNITY:
        {competitor_analysis.recommended_product_opportunity}

        Produce the ranked roadmap.

        After selecting the top-priority feature, request
        human approval before treating the feature as approved.
        """
    )

    # Human-in-the-loop approval
    while result.interruptions:

        print("\n" + "!" * 70)
        print("HUMAN APPROVAL REQUIRED")
        print("!" * 70)

        state = result.to_state()

        for interruption in result.interruptions:

            print(
                f"\nApproval tool: "
                f"{interruption.name}"
            )

            decision = input(
                "\nApprove the top product priority? "
                "(yes/no): "
            ).strip().lower()

            if decision in ["yes", "y"]:

                state.approve(interruption)

                print(
                    "\n✅ Product Manager approved "
                    "the recommendation."
                )

            else:

                state.reject(interruption)

                print(
                    "\n❌ Product Manager rejected "
                    "the recommendation."
                )

        print("\nResuming prioritisation workflow...")

        result = Runner.run_sync(
            prioritisation_agent,
            state
        )

    analysis = result.final_output

    print(
        f"\nTop Priority Feature: "
        f"{analysis.top_priority_feature}"
    )

    return analysis


def request_final_confirmation(
    prioritisation_analysis
):

    print("\n" + "=" * 70)
    print("ROADMAP DECISION")
    print("=" * 70)

    print(
        f"\nRecommended Feature: "
        f"{prioritisation_analysis.top_priority_feature}"
    )

    print(
        "\nThe feature has passed the AI prioritisation "
        "and human approval stage."
    )

    decision = input(
        "\nContinue to PRD and Sprint Planning? "
        "(yes/no): "
    ).strip().lower()

    return decision in ["yes", "y"]


def run_prd_generation(
    prioritisation_analysis,
    feedback_analysis,
    analytics_analysis
):

    print("\n" + "=" * 70)
    print("STEP 5 — PRD GENERATION")
    print("=" * 70)

    top_feature = (
        prioritisation_analysis.top_priority_feature
    )

    result = Runner.run_sync(
        prd_agent,
        f"""
        Create a complete Product Requirements Document
        for the approved TaskFlow initiative.

        APPROVED FEATURE:
        {top_feature}

        CUSTOMER EVIDENCE:
        {feedback_analysis.top_priority_issue}

        ANALYTICS EVIDENCE:
        {analytics_analysis.biggest_product_concern}

        ROADMAP CONTEXT:
        {prioritisation_analysis.roadmap_summary}

        Use the engineering constraints tool.

        The PRD must be practical, testable and suitable
        for Product, Design and Engineering review.
        """
    )

    prd = result.final_output

    print(f"\nPRD created for: {prd.feature_name}")

    print("\nProblem Statement:")
    print(prd.problem_statement)

    print("\nObjectives:")

    for objective in prd.objectives:
        print(f"- {objective}")

    return prd


def run_sprint_planning(prd):

    print("\n" + "=" * 70)
    print("STEP 6 — SPRINT PLANNING")
    print("=" * 70)

    prd_context = prd.model_dump_json(
        indent=2
    )

    result = Runner.run_sync(
        sprint_agent,
        f"""
        Create a realistic sprint plan based on the
        following approved Product Requirements Document.

        PRD:

        {prd_context}

        Use the sprint capacity tool.

        Respect all:
        - engineering constraints
        - dependencies
        - accessibility requirements
        - security requirements
        - sprint capacity limits

        Do not exceed the available story-point capacity
        in any sprint.
        """
    )

    sprint_plan = result.final_output

    print(
        f"\nNumber of Sprints: "
        f"{sprint_plan.number_of_sprints}"
    )

    print(
        f"Total Story Points: "
        f"{sprint_plan.total_story_points}"
    )

    for sprint in sprint_plan.sprints:

        print(
            f"\nSprint {sprint.sprint_number}"
        )

        print(
            f"Goal: {sprint.sprint_goal}"
        )

        print(
            f"Capacity: {sprint.capacity}"
        )

        print(
            f"Planned Points: "
            f"{sprint.total_story_points}"
        )

    return sprint_plan


def run_complete_workflow():

    print("\n")
    print("#" * 70)
    print("TASKFLOW — AI PRODUCT MANAGER")
    print("END-TO-END MULTI-AGENT WORKFLOW")
    print("#" * 70)

    # STEP 1
    feedback_analysis = (
        run_feedback_analysis()
    )

    # STEP 2
    analytics_analysis = (
        run_product_analytics(
            feedback_analysis
        )
    )

    # STEP 3
    competitor_analysis = (
        run_competitor_research(
            feedback_analysis,
            analytics_analysis
        )
    )

    # STEP 4
    prioritisation_analysis = (
        run_prioritisation(
            feedback_analysis,
            analytics_analysis,
            competitor_analysis
        )
    )

    # SECOND HUMAN CHECKPOINT
    approved_to_continue = (
        request_final_confirmation(
            prioritisation_analysis
        )
    )

    if not approved_to_continue:

        print(
            "\nWorkflow stopped by Product Manager."
        )

        print(
            "No PRD or Sprint Plan was generated."
        )

        return

    # STEP 5
    prd = run_prd_generation(
        prioritisation_analysis,
        feedback_analysis,
        analytics_analysis
    )

    # STEP 6
    sprint_plan = run_sprint_planning(
        prd
    )

    # FINAL SUMMARY
    print("\n")
    print("#" * 70)
    print("WORKFLOW COMPLETE")
    print("#" * 70)

    print(
        f"\nApproved Product Initiative: "
        f"{prioritisation_analysis.top_priority_feature}"
    )

    print(
        f"PRD Generated: "
        f"{prd.feature_name}"
    )

    print(
        f"Sprints Planned: "
        f"{sprint_plan.number_of_sprints}"
    )

    print(
        f"Total Story Points: "
        f"{sprint_plan.total_story_points}"
    )

    print(
        "\n✅ Customer evidence analysed"
    )

    print(
        "✅ Product analytics analysed"
    )

    print(
        "✅ Competitor market researched"
    )

    print(
        "✅ Feature roadmap prioritised"
    )

    print(
        "✅ Human approval obtained"
    )

    print(
        "✅ PRD generated"
    )

    print(
        "✅ Sprint plan generated"
    )