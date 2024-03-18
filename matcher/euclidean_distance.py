# Unique ID: 5345877c-c30e-4f12-b5ee-afd2b60f7421
import numpy as np

def calculate_euclidean_distance(feature1: np.ndarray, feature2: np.ndarray) -> float:
    """
    Calculates the Euclidean distance between two feature vectors.

    Parameters:
    - feature1: The first feature vector.
    - feature2: The second feature vector.

    Returns:
    - The Euclidean distance between the two feature vectors.
    """
    try:
        # Ensure feature vectors are 1D arrays and of the same length
        feature1 = np.ravel(feature1)
        feature2 = np.ravel(feature2)
        if len(feature1) != len(feature2):
            raise ValueError("Feature vectors must have the same length.")

        # Calculate the Euclidean distance
        distance = np.linalg.norm(feature1 - feature2)

        return distance

    except ValueError as ve:
        # Log and re-raise the ValueError
        print(f"ValueError occurred during Euclidean distance calculation: {str(ve)}")
        raise
    except Exception as e:
        # Log and raise any other exceptions
        print(f"Error occurred during Euclidean distance calculation: {str(e)}")
        raise

    
