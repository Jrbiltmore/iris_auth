# Unique ID: 57c1282f-7f71-45b8-be4b-86ef2a14c6d8
import json

def load_config(config_file_path: str) -> dict:
    """
    Loads a configuration file in JSON format.

    Parameters:
    - config_file_path: The path to the configuration file.

    Returns:
    - A dictionary containing the configuration settings.
    """
    try:
        # Load the configuration file
        with open(config_file_path, 'r') as file:
            config_data = json.load(file)
        
        return config_data

    except Exception as e:
        print(f"Error occurred while loading the configuration file: {e}")
        raise

    
