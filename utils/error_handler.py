# Unique ID: 08f6c928-71ea-4f1f-af67-69670144afd7
import logging

def log_error(error_message: str) -> None:
    """
    Logs an error message to the console.

    Parameters:
    - error_message: The error message to log.
    """
    try:
        # Create a logger
        logger = logging.getLogger(__name__)

        # Log the error message
        logger.error(error_message)

    except Exception as e:
        print(f"Error occurred while logging the error: {e}")
        raise

    
