from pathlib import Path

import pandas as pd
from agents import function_tool


@function_tool
def load_engineering_constraints() -> str:
    """
    Load the current engineering and technical constraints
    that must be considered when creating TaskFlow PRDs.
    """

    project_root = Path(__file__).resolve().parent.parent

    constraints_file = (
        project_root
        / "data"
        / "engineering_constraints.csv"
    )

    df = pd.read_csv(constraints_file)

    return df.to_string(index=False)
