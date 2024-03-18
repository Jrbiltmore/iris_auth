# Unique ID: 535a0d36-f62d-4442-9858-df6f2d7e83f7
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

def calculate_cosine_similarity(feature1: np.ndarray, feature2: np.ndarray) -> float:
    """
    Calculates the cosine similarity between two feature vectors.

    Parameters:
    - feature1: The first feature vector.
    - feature2: The second feature vector.

    Returns:
    - The cosine similarity between the two feature vectors.
    """
    try:
        # Reshape the feature vectors if needed
        if len(feature1.shape) == 1:
            feature1 = feature1.reshape(1, -1)
        if len(feature2.shape) == 1:
            feature2 = feature2.reshape(1, -1)

        # Calculate the cosine similarity
        similarity = cosine_similarity(feature1, feature2)[0, 0]

        return similarity

    except ValueError as ve:
        # Log and re-raise the ValueError
        print(f"ValueError occurred during cosine similarity calculation: {str(ve)}")
        raise
    except Exception as e:
        # Log and raise any other exceptions
        print(f"Error occurred during cosine similarity calculation: {str(e)}")
        raise

    
