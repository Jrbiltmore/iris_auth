# Unique ID: f61ce7d8-d441-4d71-9b24-d6dc4041c806
import logging

def setup_logger(log_file_path: str) -> None:
    """
    Sets up logging configuration.

    Parameters:
    - log_file_path: The path to the log file.
    """
    try:
        # Configure logging
        logging.basicConfig(filename=log_file_path,
                            level=logging.DEBUG,
                            format='%(asctime)s - %(levelname)s - %(message)s')

    except Exception as e:
        print(f"Error occurred while setting up logger: {e}")
        raise

    
