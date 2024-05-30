class Camera:
    def __init__(self, resolution="1080p", night_vision=False, motion_detection=False):
        self.resolution = resolution
        self.night_vision = night_vision
        self.motion_detection = motion_detection

    def __str__(self):
        return f"Camera: Resolution={self.resolution}, Night Vision={self.night_vision}, Motion Detection={self.motion_detection}"

class CameraBuilder:
    def __init__(self):
        self.camera = Camera()

    def set_resolution(self, resolution):
        self.camera.resolution = resolution
        return self

    def enable_night_vision(self):
        self.camera.night_vision = True
        return self

    def enable_motion_detection(self):
        self.camera.motion_detection = True
        return self

    def build(self):
        return self.camera
