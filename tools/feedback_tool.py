from pathlib import Path

import pandas as pd
from agents import function_tool


@function_tool
def load_customer_feedback() -> str:
    """
    Load customer feedback from the TaskFlow customer feedback CSV file.
    """

    project_root = Path(__file__).resolve().parent.parent
    feedback_file = project_root / "data" / "customer_feedback.csv"

    df = pd.read_csv(feedback_file)

    return df.to_string(index=False)