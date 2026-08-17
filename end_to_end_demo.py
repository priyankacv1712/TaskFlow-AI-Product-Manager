from agents import set_tracing_disabled

set_tracing_disabled(True)

from workflows.end_to_end_workflow import (
    run_complete_workflow,
)


if __name__ == "__main__":
    run_complete_workflow()