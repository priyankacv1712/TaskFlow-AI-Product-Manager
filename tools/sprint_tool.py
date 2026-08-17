from agents import function_tool


@function_tool
def get_sprint_capacity() -> str:
    """
    Return the current engineering capacity available
    for the TaskFlow onboarding initiative.
    """

    return """
    Current Sprint Planning Constraints:

    - Maximum onboarding engineering capacity: 8 story points per sprint.
    - Authentication and account verification must remain unchanged.
    - Existing React component library must be used.
    - Major database schema changes are not allowed.
    - Accessibility support is mandatory.
    - Existing user accounts must remain compatible.
    """