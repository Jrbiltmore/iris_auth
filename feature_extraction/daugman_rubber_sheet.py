# Unique ID: 233d913e-ad8c-4f4a-a887-db93d3751283
import numpy as np
from scipy.ndimage import map_coordinates

def daugman_rubber_sheet(image: np.ndarray, iris_center: tuple, iris_radius: int, pupil_center: tuple, pupil_radius: int,
                         output_shape: tuple) -> np.ndarray:
    """
    Applies Daugman's rubber sheet model to normalize an iris image.

    Parameters:
    - image: The input iris image in numpy array format.
    - iris_center: The coordinates (x, y) of the iris center.
    - iris_radius: The radius of the iris.
    - pupil_center: The coordinates (x, y) of the pupil center.
    - pupil_radius: The radius of the pupil.
    - output_shape: The desired output shape of the normalized iris image.

    Returns:
    - The normalized iris image.
    """
    # Generate polar coordinates grid
    y, x = np.indices(output_shape)
    theta = np.arctan2(y - iris_center[1], x - iris_center[0])
    rho = np.sqrt((x - iris_center[0]) ** 2 + (y - iris_center[1]) ** 2)

    # Map polar coordinates to Cartesian coordinates
    x_mapped = iris_center[0] + rho * np.cos(theta)
    y_mapped = iris_center[1] + rho * np.sin(theta)

    # Ensure mapped coordinates are within image bounds
    x_mapped = np.clip(x_mapped, 0, image.shape[1] - 1)
    y_mapped = np.clip(y_mapped, 0, image.shape[0] - 1)

    # Interpolate pixel values using mapped Cartesian coordinates
    output_image = map_coordinates(image, [y_mapped, x_mapped], order=3, mode='constant', cval=0)

    return output_image.astype(np.uint8)

    
