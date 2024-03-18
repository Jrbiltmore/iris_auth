# Unique ID: 258d7444-2a61-4238-808c-4047f764a02f
import cv2
import numpy as np

def check_image_quality(image: np.ndarray, min_resolution: tuple = (100, 100), max_noise_ratio: float = 0.1,
                        min_sharpness: float = 30.0, min_contrast: float = 0.1,
                        min_brightness: float = 0.1, max_brightness: float = 0.9) -> bool:
    """
    Checks the quality of the captured image based on resolution, noise, sharpness, contrast, and brightness.

    Parameters:
    - image: The input image in numpy array format (BGR color space).
    - min_resolution: Minimum acceptable resolution for the image (width, height).
    - max_noise_ratio: Maximum acceptable ratio of noisy pixels to total pixels.
    - min_sharpness: Minimum acceptable sharpness value (in degrees).
    - min_contrast: Minimum acceptable contrast value (0-1).
    - min_brightness: Minimum acceptable brightness value (0-1).
    - max_brightness: Maximum acceptable brightness value (0-1).

    Returns:
    - True if the image passes the quality checks, False otherwise.
    """
    # Check resolution
    if image.shape[0] < min_resolution[1] or image.shape[1] < min_resolution[0]:
        print("Image resolution is too low.")
        return False

    # Calculate noise ratio
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    num_noisy_pixels = np.sum(gray_image < 10)  # Count pixels with low intensity as noise
    total_pixels = gray_image.size
    noise_ratio = num_noisy_pixels / total_pixels

    # Check noise ratio
    if noise_ratio > max_noise_ratio:
        print("Image contains too much noise.")
        return False

    # Calculate sharpness using Laplacian operator
    sharpness = cv2.Laplacian(gray_image, cv2.CV_64F).var()

    # Check sharpness
    if sharpness < min_sharpness:
        print("Image is not sharp enough.")
        return False

    # Calculate contrast using histogram
    hist = cv2.calcHist([gray_image], [0], None, [256], [0, 256])
    cum_hist = np.cumsum(hist)
    total_pixels = cum_hist[-1]
    threshold_idx = np.where(cum_hist > total_pixels * min_contrast)[0][0]

    # Check contrast
    if threshold_idx < 10 or threshold_idx > 245:
        print("Image has low contrast.")
        return False

    # Calculate brightness using histogram
    brightness = np.mean(gray_image) / 255.0

    # Check brightness
    if brightness < min_brightness or brightness > max_brightness:
        print("Image brightness is out of acceptable range.")
        return False

    return True

# Example usage
if __name__ == "__main__":
    # Load a captured image (replace this with actual image loading logic)
    input_image = cv2.imread("captured_image.jpg")

    # Perform pre-checks on the image
    if check_image_quality(input_image):
        print("Image passed pre-checks. Ready for further processing.")
    else:
        print("Image failed pre-checks. Requires re-capture.")

    
