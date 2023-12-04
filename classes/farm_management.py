import json


class FarmManagement:
    """
    - Manages animals and crops on the farm
    - display_farm_status(): Displays the current state of the farm
    - read_animal_history(): Displays the feeding history of animals
    - read_crop_history(): Displays the watering history of crops with various substances
    """
    def __init__(self):
        self.animals = []
        self.crops = []
        self.raw_materials = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def add_crop(self, crop):
        self.crops.append(crop)

    def add_raw_materials(self, raw_materials):
        self.raw_materials.append(raw_materials)

    def display_farm_status(self):
        print("Current farm status:")
        print("Animals:")
        for animal in self.animals:
            print(f" - {animal}")
        print("Crops:")
        for crop in self.crops:
            print(f" - {crop}")
        print("Raw Materials:")
        for material in self.raw_materials:
            print(f" - {material}")
        print("<-------------------------------------------->\n")

    def read_animal_history(self):
        try:
            with open("data/animal_history.json", "r") as history_file:
                history_data = json.load(history_file)
                print("Animal history:")
                for animal_name, animal_history in history_data.items():
                    print(f" - Name: {animal_name}")
                    for action in animal_history:
                        print(f"- Action: {action['action']} - Food: {action['food']} "
                              f"- Date: {action['date']}")
        except FileNotFoundError:
            print("File for animal history does not exist.")
        print("<-------------------------------------------->\n")

    def read_crop_history(self):
        try:
            with open("data/crop_history.json", "r") as history_file:
                history_data = json.load(history_file)
                print("Crop history:")
                for crop_name, crop_history in history_data.items():
                    print(f" - Name: {crop_name}")
                    for action in crop_history:
                        print(f"- Action: {action['action']} - Substance: {action['substance']} "
                              f"- Date: {action['date']}")
        except FileNotFoundError:
            print("File for crop history does not exist.")
        print("<-------------------------------------------->\n")
