import time
import random
from mediator.mediator import ConcreteMediator, Camera, Controller
from decorator.decorator import Camera as BasicCamera, NightVisionCamera, MotionDetectionCamera
from builder.builder import CameraBuilder
from database.animal_count_db import AnimalCountDB, AnimalController
from interface.personel_screen import PersonelScreen
from interface.government_screen import GovernmentScreen
from animal_cam_machine import AnimalCamMachine

# Setting up Mediator pattern
print("Setting up Mediator pattern...")
time.sleep(3)
mediator = ConcreteMediator()
camera = Camera(mediator)
controller = Controller(mediator)

mediator.add_camera(camera)
mediator.add_controller(controller)

# Simulate animal detection
print("Simulating animal detection...")
time.sleep(3)

class AnimalCamera(Camera):
    def capture(self):
        choice = input("Press '1' for bear, '2' for random animal: ") # Ask user for choice
        if choice == '1':
            animal = "bear"
        elif choice == '2':
            animals = ["cat", "dog", "bird", "raccoon"] # List of animals
            animal = random.choice(animals) # Select a random animal
        else:
            print("Invalid choice. Defaulting to random animal.")
            animals = ["cat", "dog", "bird", "raccoon", "bear"] # List of animals
            animal = random.choice(animals) # Select a random animal
        
        print(f"Animal detected: {animal.capitalize()}.")
        self.mediator.send(f"{animal.capitalize()} detected.", self)
        return animal

animal_camera = AnimalCamera(mediator)
mediator.add_camera(animal_camera)

animal = animal_camera.capture()  # Assign the captured animal to a variable

# Setting up Decorator pattern
print("Setting up Decorator pattern...")
time.sleep(3)
basic_camera = BasicCamera()
night_vision_camera = NightVisionCamera(basic_camera)
motion_detection_camera = MotionDetectionCamera(night_vision_camera)

motion_detection_camera.capture()

# Setting up Builder pattern
print("Setting up Builder pattern...")
time.sleep(3)
camera_builder = CameraBuilder()
custom_camera = camera_builder.set_resolution("4K").enable_night_vision().enable_motion_detection().build()

print("Custom camera built: ", custom_camera)

# Setting up Database and Controller
print("Setting up Database and Controller...")
time.sleep(3)
db = AnimalCountDB()
animal_controller = AnimalController(db)
animal_controller.dejectAnimal(animal) # Use the captured animal here

# Personel Screen
print("Showing Personel Screen...")
time.sleep(3)
personel_screen = PersonelScreen()
personel_screen.show()

# Government Screen
print("Showing Government Screen...")
time.sleep(3)
government_screen = GovernmentScreen()
government_screen.show()

# Feeding the animal
print("Feeding the animal...")
time.sleep(2)
animal_cam_machine = AnimalCamMachine()
animal_cam_machine.feed()
print("Feeding completed.")

