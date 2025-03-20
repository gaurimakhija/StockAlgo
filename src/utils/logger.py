import logging
import os
import sys

class LoggerManager:
    """A professional logging system to handle logging and exceptions."""

    def __init__(self, log_file="logs/app.log"):
        """Initializes the logging system with a structured log file."""
        os.makedirs(os.path.dirname(log_file), exist_ok=True)  # Create 'logs/' folder if missing

        logging.basicConfig(
            filename=log_file,
            level=logging.INFO,
            format="%(asctime)s - %(levelname)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )

    def log_info(self, message: str):
        """Logs an informational message."""
        logging.info(message)
        print(f"[INFO] {message}")

    def log_warning(self, message: str):
        """Logs a warning message."""
        logging.warning(message)
        print(f"[WARNING] {message}")

    def log_error(self, message: str):
        """Logs an error message."""
        logging.error(message)
        print(f"[ERROR] {message}", file=sys.stderr)

    def raise_exception(self, message: str):
        """Logs an error and raises an exception."""
        self.log_error(message)
        raise Exception(message)

