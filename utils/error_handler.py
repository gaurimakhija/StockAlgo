import traceback
import logging
from pathlib import Path

class ErrorHandler:
    def __init__(self, log_file: Path = "error_log.txt"):
        """Initialize the error handler with an optional log file."""
        self.log_file = Path(log_file).resolve()
        logging.basicConfig(
            filename=self.log_file, 
            level=logging.ERROR, 
            format="%(asctime)s - %(levelname)s - %(message)s"
        )

    def log_error(self, error: Exception, custom_message: str = ""):
        """Logs an error with an optional custom message."""
        error_details = traceback.format_exc()
        message = f"{custom_message}\n{error_details}" if custom_message else error_details
        logging.error(message)
        print(f"Error logged: {custom_message or error}")

    def try_except(self, func):
        """Decorator to automatically catch and log errors in any function."""
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                self.log_error(e, f"Error in function: {func.__name__}")
        return wrapper
