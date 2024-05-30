import random
class Mediator:
    def send(self, message, colleague):
        pass

class ConcreteMediator(Mediator):
    def __init__(self):
        self.cameras = []
        self.controllers = []

    def add_camera(self, camera):
        self.cameras.append(camera)

    def add_controller(self, controller):
        self.controllers.append(controller)

    def send(self, message, colleague):
        if isinstance(colleague, Camera):
            for controller in self.controllers:
                controller.receive(message)
        elif isinstance(colleague, Controller):
            for camera in self.cameras:
                camera.receive(message)

class Colleague:
    def __init__(self, mediator):
        self.mediator = mediator

class Camera(Colleague):
    def capture(self):
        animals = ["cat", "dog", "bird", "raccoon", "bear"] # List of animals
        animal = random.choice(animals) # Select a random animal
        print(f"Camera: {animal.capitalize()} detected.")
        self.mediator.send(f"{animal.capitalize()} detected.", self)

    def receive(self, message):
        print(f"Camera received: {message}")

class Controller(Colleague):
    def process(self, message):
        if "bear" in message.lower():
            print("Controller: Bear detected! Alerting authorities.")
        else:
            print("Controller: No dangerous animal detected.")


    def receive(self, message):
        self.process(message)
