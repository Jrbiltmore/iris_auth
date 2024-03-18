# Unique ID: 8187b7df-8caf-487c-a2de-216c381779a8
import cv2

def detect_edges(image: np.ndarray, threshold1: int = 100, threshold2: int = 200) -> np.ndarray:
    """
    Detects edges in an image using the Canny edge detection algorithm.

    Parameters:
    - image: The input image as a NumPy array.
    - threshold1: The lower threshold for the hysteresis procedure.
    - threshold2: The higher threshold for the hysteresis procedure.

    Returns:
    - The edge-detected image as a binary image.
    """
    try:
        # Convert the image to grayscale
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Apply Gaussian blur to reduce noise
        blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)

        # Detect edges using the Canny edge detector
        edges = cv2.Canny(blurred_image, threshold1, threshold2)

        return edges

    except Exception as e:
        print(f"Error occurred during edge detection: {e}")
        raise

    
