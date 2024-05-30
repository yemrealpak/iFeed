class AnimalCountDB:
    def __init__(self):
        self.animalData = []

    def save_animal_data(self, data):
        self.animalData.append(data)
        print(f"Data saved: {data}")

    def animal_data_to_gov(self):
        print("Sending animal data to government:")
        for data in self.animalData:
            print(data)

class AnimalController:
    def __init__(self, db):
        self.db = db

    def dejectAnimal(self, animal):
        if animal == "dangerous":
            print("Dangerous animal detected!")
            self.db.save_animal_data("Dangerous animal detected")
            self.dejectAndDbController(animal)

    def dejectAndDbController(self, animal):
        self.db.animal_data_to_gov()
