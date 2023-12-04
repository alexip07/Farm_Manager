from classes.resources import Resource
import json
from datetime import datetime


class Animal(Resource):
    """
    - feed(): Feeds the animal and updates the history
    - set_health(): Updates the health status of the animal
    - add_quantity(): Increases the number of animals and automatically updates the JSON file
    - reduce_quantity(): Reduces the number of animals and automatically updates the JSON file
    - The modify_quantity() method was created to make the code easier to read,
    it is used for both addition and subtraction and is also present in the Crop class
    - - The add_to_farm() method updates the JSON file with the new animals
    """

    def __init__(self, name, type, quantity, health="", food=""):
        super().__init__(name, quantity)
        self.type = type
        self.health = health
        self.food = food
        self.history = []

    def feed(self, food):
        self.food = food
        self.history.append({"action": "feeding", "food": food,
                             "date": str(datetime.now().replace(second=0, microsecond=0))})
        try:
            with open(f"data/animal_history.json", "r") as history_file:
                history_data = json.load(history_file)
        except FileNotFoundError:
            # If the file does not exist, create an empty dictionary for history_data
            history_data = {}

        # Save the data in history_data
        history_data[self.name] = self.history

        # Save the history in the JSON file
        with open(f"data/animal_history.json", "w") as history_file:
            json.dump(history_data, history_file, indent=4)

    def set_health(self, health):
        self.health = health

        # Update the JSON file with the current health status of the animal
        try:
            with open("data/farm.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            print("The 'farm.json' file does not exist.")
            return

        if self.name in data:
            data[self.name]["health"] = self.health

            # Save the updated data in the JSON file
            with open("data/farm.json", "w") as data_file:
                json.dump(data, data_file, indent=4)

    def add_quantity(self, quantity):
        self.quantity += quantity

        self.modify_quantity()

    def reduce_quantity(self, quantity):
        self.quantity -= quantity

        self.modify_quantity()

    def modify_quantity(self):

        try:
            with open("data/farm.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            print("The 'farm.json' file does not exist.")
            return

        if self.name in data:
            data[self.name]["quantity"] = self.quantity

            with open("data/farm.json", "w") as data_file:
                json.dump(data, data_file, indent=4)

    def add_to_farm(self, farm_management):
        farm_management.add_animal(self)

        new_data = {self.name: {"type": self.type, "quantity": self.quantity}}
        try:
            with open("data/farm.json", "r") as data_file:
                data = json.load(data_file)

        except FileNotFoundError:
            with open("data/farm.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)

        else:
            data.update(new_data)
            with open("data/farm.json", "w") as data_file:
                json.dump(data, data_file, indent=4)

    def __str__(self):
        return f"{self.name} ({self.type}) - Health: {self.health} - Quantity: {self.quantity} units"
