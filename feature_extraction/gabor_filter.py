# Unique ID: 655f8c54-6732-4e08-bbcc-fadcf498f1ac
import numpy as np
import cv2

def apply_gabor_filter(image: np.ndarray, kernel_size: tuple, sigma: float, theta: float, lambd: float, gamma: float) -> np.ndarray:
    """
    Applies a Gabor filter to an image.

    Parameters:
    - image: The input image in numpy array format.
    - kernel_size: The size of the Gabor kernel (height, width).
    - sigma: The standard deviation of the Gaussian envelope.
    - theta: The orientation of the normal to the parallel stripes of the Gabor function.
    - lambd: The wavelength of the sinusoidal factor.
    - gamma: The spatial aspect ratio.

    Returns:
    - The filtered image.
    """
    try:
        # Create a Gabor kernel
        kernel = cv2.getGaborKernel(kernel_size, sigma, theta, lambd, gamma)

        # Apply the Gabor filter to the image
        filtered_image = cv2.filter2D(image, cv2.CV_64F, kernel)

        return filtered_image

    except Exception as e:
        # Log and raise any exceptions
        print(f"Error occurred during Gabor filter application: {str(e)}")
        raise

    
