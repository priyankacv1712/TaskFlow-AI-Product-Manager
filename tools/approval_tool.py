from agents import function_tool


@function_tool(needs_approval=True)
def approve_product_feature(
    feature_name: str,
    reason: str
) -> str:
    """
    Approve a prioritised product feature before PRD
    and sprint planning continue.
    """

    return (
        f"Feature '{feature_name}' has been approved "
        f"for product planning. Reason: {reason}"
    )