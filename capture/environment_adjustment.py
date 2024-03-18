# Unique ID: 9da08bb7-a1b3-497c-a2c1-241acbe003de
import cv2
import numpy as np

def adjust_environment(image: np.ndarray, brightness_factor: float = 1.0, contrast_factor: float = 1.0,
                       gamma: float = 1.0, sharpen: bool = False, denoise: bool = False) -> np.ndarray:
    """
    Adjusts the environment of the captured image.

    Parameters:
    - image: The input image in numpy array format (BGR color space).
    - brightness_factor: Factor to adjust image brightness (default: 1.0, no adjustment).
    - contrast_factor: Factor to adjust image contrast (default: 1.0, no adjustment).
    - gamma: Gamma correction factor (default: 1.0, no correction).
    - sharpen: Flag to enable sharpening (default: False).
    - denoise: Flag to enable denoising (default: False).

    Returns:
    - The adjusted image.
    """
    # Convert image to LAB color space for better adjustments
    lab_image = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)

    # Adjust brightness and contrast
    lab_image = adjust_brightness_contrast(lab_image, brightness_factor, contrast_factor)

    # Apply gamma correction
    adjusted_image = apply_gamma_correction(lab_image, gamma)

    # Apply sharpening
    if sharpen:
        adjusted_image = sharpen_image(adjusted_image)

    # Apply denoising
    if denoise:
        adjusted_image = denoise_image(adjusted_image)

    # Convert back to BGR color space
    adjusted_image_bgr = cv2.cvtColor(adjusted_image, cv2.COLOR_LAB2BGR)

    return adjusted_image_bgr

def adjust_brightness_contrast(lab_image: np.ndarray, brightness_factor: float, contrast_factor: float) -> np.ndarray:
    """
    Adjusts the brightness and contrast of the LAB color image.

    Parameters:
    - lab_image: The input LAB color image.
    - brightness_factor: Factor to adjust image brightness.
    - contrast_factor: Factor to adjust image contrast.

    Returns:
    - The adjusted LAB color image.
    """
    l_channel, a_channel, b_channel = cv2.split(lab_image)
    
    # Adjust brightness
    l_channel = cv2.add(l_channel, int(50 * brightness_factor))

    # Adjust contrast
    l_channel = cv2.multiply(l_channel, contrast_factor)

    # Clip pixel intensities to [0, 255] range
    l_channel = np.clip(l_channel, 0, 255)

    return cv2.merge([l_channel, a_channel, b_channel])

def apply_gamma_correction(lab_image: np.ndarray, gamma: float) -> np.ndarray:
    """
    Applies gamma correction to the LAB color image.

    Parameters:
    - lab_image: The input LAB color image.
    - gamma: Gamma correction factor.

    Returns:
    - The gamma-corrected LAB color image.
    """
    # Split LAB channels
    l_channel, a_channel, b_channel = cv2.split(lab_image)

    # Apply gamma correction to the L channel
    l_channel = cv2.pow(l_channel / 255.0, gamma) * 255.0

    return cv2.merge([l_channel, a_channel, b_channel])

def sharpen_image(image: np.ndarray) -> np.ndarray:
    """
    Sharpens the input image using a sharpening filter.

    Parameters:
    - image: The input image in BGR color space.

    Returns:
    - The sharpened image.
    """
    # Create a sharpening kernel
    kernel = np.array([[-1, -1, -1],
                       [-1, 9, -1],
                       [-1, -1, -1]])

    # Apply the kernel to the image
    sharpened_image = cv2.filter2D(image, -1, kernel)

    return sharpened_image

def denoise_image(image: np.ndarray) -> np.ndarray:
    """
    Denoises the input image using a bilateral filter.

    Parameters:
    - image: The input image in BGR color space.

    Returns:
    - The denoised image.
    """
    # Apply bilateral filter for noise reduction while preserving edges
    denoised_image = cv2.bilateralFilter(image, d=9, sigmaColor=75, sigmaSpace=75)

    return denoised_image

# Example usage
if __name__ == "__main__":
    # Load a captured image (replace this with actual image loading logic)
    input_image = cv2.imread("captured_image.jpg")

    # Adjust environment with custom parameters
    adjusted_image = adjust_environment(input_image, brightness_factor=1.2, contrast_factor=1.2, gamma=1.2, 
                                         sharpen=True, denoise=True)

    # Save adjusted image (replace this with actual saving logic)
    cv2.imwrite("adjusted_image.jpg", adjusted_image)

    print("Environment adjustment completed.")
