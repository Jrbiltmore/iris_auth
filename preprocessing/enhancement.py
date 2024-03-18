# Unique ID: b331ce6a-c530-4762-b5a1-cce9cefc194a
import cv2

def enhance_image(image: np.ndarray, alpha: float = 1.5, beta: float = 25) -> np.ndarray:
    """
    Enhances the contrast and brightness of an image.

    Parameters:
    - image: The input image as a NumPy array.
    - alpha: The contrast adjustment factor. Higher values increase contrast. Default is 1.5.
    - beta: The brightness adjustment factor. Higher values increase brightness. Default is 25.

    Returns:
    - The enhanced image as a NumPy array.
    """
    try:
        # Convert the image to grayscale
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Apply contrast and brightness adjustment
        enhanced_image = cv2.convertScaleAbs(gray_image, alpha=alpha, beta=beta)

        return enhanced_image

    except Exception as e:
        print(f"Error occurred during image enhancement: {e}")
        raise
