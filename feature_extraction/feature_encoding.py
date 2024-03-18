# Unique ID: cb2dbe21-5c85-4fdc-a9fc-7e5217718083
import numpy as np
from sklearn.preprocessing import StandardScaler

def encode_features(features: np.ndarray) -> np.ndarray:
    """
    Encodes extracted iris features for further processing.

    Parameters:
    - features: An array of extracted iris features.

    Returns:
    - Encoded iris features ready for use in recognition algorithms.
    """
    try:
        # Check if features array is empty
        if len(features) == 0:
            raise ValueError("Empty features array provided.")

        # Initialize a StandardScaler object to standardize features
        scaler = StandardScaler()

        # Fit the scaler to the features and transform them
        encoded_features = scaler.fit_transform(features)

        return encoded_features

    except ValueError as ve:
        # Log and re-raise the ValueError
        print(f"ValueError occurred during feature encoding: {str(ve)}")
        raise
    except Exception as e:
        # Log and raise any other exceptions
        print(f"Error occurred during feature encoding: {str(e)}")
        raise

    
