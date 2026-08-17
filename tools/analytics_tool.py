from pathlib import Path

import pandas as pd
from agents import function_tool


@function_tool
def load_product_metrics() -> str:
    """
    Load TaskFlow product usage and performance metrics.
    """

    project_root = Path(__file__).resolve().parent.parent
    metrics_file = project_root / "data" / "product_metrics.csv"

    df = pd.read_csv(metrics_file)

    return df.to_string(index=False)
