# Unique ID: 98ac23f1-0aa1-4aed-b7a1-02f935562e91
def calculate_hamming_distance(feature1: str, feature2: str) -> int:
    """
    Calculates the Hamming distance between two binary strings.

    Parameters:
    - feature1: The first binary string.
    - feature2: The second binary string.

    Returns:
    - The Hamming distance between the two binary strings.
    """
    # Ensure the binary strings have the same length
    if len(feature1) != len(feature2):
        raise ValueError("Binary strings must have the same length.")

    # Calculate the Hamming distance
    distance = sum(c1 != c2 for c1, c2 in zip(feature1, feature2))

    return distance

    
