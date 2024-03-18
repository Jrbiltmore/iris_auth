# Unique ID: 8e398966-dd4c-4e87-a276-ea88cd6d6c17
import numpy as np
from .cosine_similarity import calculate_cosine_similarity
from .euclidean_distance import calculate_euclidean_distance

def match(feature1: np.ndarray, feature2: np.ndarray, method: str = 'cosine') -> float:
    """
    Matches two feature vectors using the specified method.

    Parameters:
    - feature1: The first feature vector.
    - feature2: The second feature vector.
    - method: The method to use for matching ('cosine' or 'euclidean'). Default is 'cosine'.

    Returns:
    - The similarity/distance score between the two feature vectors.
    """
    try:
        if method == 'cosine':
            similarity = calculate_cosine_similarity(feature1, feature2)
        elif method == 'euclidean':
            similarity = -calculate_euclidean_distance(feature1, feature2)
        else:
            raise ValueError("Invalid method. Choose either 'cosine' or 'euclidean'.")

        return similarity

    except ValueError as ve:
        print(f"ValueError occurred during matching: {ve}")
        raise
    except Exception as e:
        print(f"Error occurred during matching: {e}")
        raise
