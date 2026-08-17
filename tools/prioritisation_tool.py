from pathlib import Path

import pandas as pd
from agents import function_tool


@function_tool
def calculate_feature_priorities() -> str:
    """
    Load TaskFlow feature candidates and calculate a RICE-style
    priority score for each feature.
    """

    project_root = Path(__file__).resolve().parent.parent

    feature_file = (
        project_root
        / "data"
        / "feature_candidates.csv"
    )

    df = pd.read_csv(feature_file)

    df["rice_score"] = (
        df["reach"]
        * df["impact"]
        * df["confidence"]
        / df["effort"]
    )

    df = df.sort_values(
        by="rice_score",
        ascending=False
    )

    return df.to_string(index=False)