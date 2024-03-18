# Unique ID: 262082c7-bb7d-4ead-bd22-c03716874cc1
import numpy as np
import pywt

def apply_wavelet_transform(image: np.ndarray, wavelet: str, level: int) -> tuple:
    """
    Applies a wavelet transform to an image.

    Parameters:
    - image: The input image in numpy array format.
    - wavelet: The type of wavelet to use (e.g., 'haar', 'db1', 'sym2').
    - level: The level of decomposition.

    Returns:
    - The coefficients of the wavelet transform (cA, (cH, cV, cD) * level).
    """
    try:
        # Apply the wavelet transform to the image
        coeffs = pywt.wavedec2(image, wavelet, level=level)

        return coeffs

    except Exception as e:
        # Log and raise any exceptions
        print(f"Error occurred during wavelet transform application: {str(e)}")
        raise

    
