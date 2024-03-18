# Unique ID: 717fbb94-c50f-409e-ad96-a1f89c3a4f11
import cv2
import numpy as np

def detect_faces(image: np.ndarray) -> list:
    """
    Detects faces in the given image using Haar cascade classifier.

    Parameters:
    - image: The input image in numpy array format (BGR color space).

    Returns:
    - A list of tuples containing the coordinates (x, y, w, h) of detected faces.
    """
    # Load the pre-trained Haar cascade classifier for face detection
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Convert the image to grayscale for face detection
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces in the grayscale image
    faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    return faces

def draw_faces(image: np.ndarray, faces: list) -> np.ndarray:
    """
    Draws rectangles around detected faces on the input image.

    Parameters:
    - image: The input image in numpy array format (BGR color space).
    - faces: A list of tuples containing the coordinates (x, y, w, h) of detected faces.

    Returns:
    - The image with rectangles drawn around detected faces.
    """
    # Draw rectangles around detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

    return image

# Example usage
if __name__ == "__main__":
    # Load a captured image (replace this with actual image loading logic)
    input_image = cv2.imread("captured_image.jpg")

    # Detect faces in the image
    detected_faces = detect_faces(input_image)

    # Check if any faces were detected
    if detected_faces:
        print("Faces detected!")

        # Draw rectangles around detected faces
        image_with_faces = draw_faces(input_image.copy(), detected_faces)

        # Display the image with detected faces
        cv2.imshow("Detected Faces", image_with_faces)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("No faces detected.")

    
