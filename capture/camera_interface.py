# Unique ID: fdb58e96-e781-4b5e-8581-bc28461e4a52
import cv2
import os
from typing import List

class CameraInterface:
    def __init__(self, camera_index=0):
        self.camera_index = camera_index
        self.camera = cv2.VideoCapture(camera_index)
        if not self.camera.isOpened():
            raise Exception(f"Camera at index {camera_index} initialization failed.")

    def set_camera_properties(self, properties: dict):
        for prop, value in properties.items():
            if hasattr(cv2, prop):
                self.camera.set(getattr(cv2, prop), value)
            else:
                raise AttributeError(f"Property {prop} not recognized.")

    def capture_image(self) -> cv2.Mat:
        ret, frame = self.camera.read()
        if not ret:
            raise Exception("Failed to capture image.")
        return frame

    def capture_series_of_images(self, count: int) -> List[cv2.Mat]:
        images = []
        for _ in range(count):
            image = self.capture_image()
            images.append(image)
        return images

    def save_image(self, image: cv2.Mat, filename: str):
        if not os.path.exists('captured_images'):
            os.makedirs('captured_images')
        cv2.imwrite(os.path.join('captured_images', filename), image)

    def release_camera(self):
        self.camera.release()

if __name__ == "__main__":
    cam = CameraInterface()
    try:
        # Example: Set camera resolution
        cam.set_camera_properties({'CAP_PROP_FRAME_WIDTH': 1920, 'CAP_PROP_FRAME_HEIGHT': 1080})
        
        # Capture a single image
        image = cam.capture_image()
        cv2.imshow('Captured Image', image)
        cv2.waitKey(0)  # Wait for a key press to close the image window
        
        # Capture a series of 5 images
        series_images = cam.capture_series_of_images(5)
        for idx, img in enumerate(series_images):
            cam.save_image(img, f"image_{idx}.png")
            print(f"Saved image_{idx}.png")
            
    finally:
        cam.release_camera()
        cv2.destroyAllWindows()
