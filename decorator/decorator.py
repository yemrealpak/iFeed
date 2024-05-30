class Camera:
    def capture(self):
        print("Capturing image...")

class BasicCamera(Camera):
    pass

class CameraDecorator(Camera):
    def __init__(self, camera):
        self.camera = camera

    def capture(self):
        self.camera.capture()

class NightVisionCamera(CameraDecorator):
    def capture(self):
        print("Activating night vision mode...")
        self.camera.capture()

class MotionDetectionCamera(CameraDecorator):
    def capture(self):
        print("Starting motion detection...")
        self.camera.capture()
