import os
import logging


# ------------------------------------------------------------
# Logging configuration
# ------------------------------------------------------------
def setup_logging():
    """
    Sets up logging for the application.
    Logs are stored in /logs/app.log relative to project root.
    """
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    log_dir = os.path.join(base_dir, "logs")
    os.makedirs(log_dir, exist_ok=True)

    log_file = os.path.join(log_dir, "file_log.log")

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler(),  # Also log to console
        ],
    )
