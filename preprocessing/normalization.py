# Unique ID: 00d77cc3-f2e1-4e06-8f60-da09936a8a9d
import numpy as np

def normalize_image(image: np.ndarray) -> np.ndarray:
    """
    Normalizes the pixel values of an image to a range of [0, 1].

    Parameters:
    - image: The input image as a NumPy array.

    Returns:
    - The normalized image as a NumPy array.
    """
    try:
        # Convert the image pixel values to float
        normalized_image = image.astype(np.float32)

        # Normalize the pixel values to the range [0, 1]
        normalized_image /= 255.0

        return normalized_image

    except Exception as e:
        print(f"Error occurred during image normalization: {e}")
        raise

    
