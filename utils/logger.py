import logging
from pathlib import Path


project_root = Path(__file__).resolve().parent.parent
logs_dir = project_root / "logs"

logs_dir.mkdir(exist_ok=True)

log_file = logs_dir / "taskflow.log"


logger = logging.getLogger("taskflow")

logger.setLevel(logging.INFO)


if not logger.handlers:

    file_handler = logging.FileHandler(
        log_file,
        encoding="utf-8"
    )

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s"
    )

    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)