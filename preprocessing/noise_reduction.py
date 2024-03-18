import cv2

def reduce_noise(image: np.ndarray, kernel_size: Tuple[int, int] = (3, 3)) -> np.ndarray:
    """
    Reduces noise in an image using Gaussian blur filtering.

    Parameters:
    - image: The input image as a NumPy array.
    - kernel_size: The size of the Gaussian kernel for blurring. Default is (3, 3).

    Returns:
    - The noise-reduced image as a NumPy array.
    """
    try:
        # Apply Gaussian blur to reduce noise
        blurred_image = cv2.GaussianBlur(image, kernel_size, 0)

        return blurred_image

    except Exception as e:
        print(f"Error in noise reduction: {e}")
        raise

    
