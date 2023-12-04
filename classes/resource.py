import json


class Resource:
    """This is the base class for the Animal and Crop classes
    - Also used for storing raw materials on the farm
    """
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity
        self.history = []

    def save_raw_materials(self, farm_management):
        farm_management.add_raw_materials(self)

        new_data = {self.name: {"quantity": self.quantity}}
        try:
            with open("data/raw_materials.json", "r") as data_file:
                data = json.load(data_file)

        except FileNotFoundError:
            with open("data/raw_materials.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)

        else:
            data.update(new_data)
            with open("data/raw_materials.json", "w") as data_file:
                json.dump(data, data_file, indent=4)

    def add_quantity_raw_materials(self, quantity):
        self.quantity += quantity

        self.modify_quantity()

    def reduce_quantity_raw_materials(self, quantity):
        self.quantity -= quantity

        self.modify_quantity()

    def modify_quantity(self):
        try:
            with open("data/raw_materials.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            print("File 'raw_materials.json' does not exist.")
            return

        if self.name in data:
            data[self.name]["quantity"] = self.quantity

            with open("data/raw_materials.json", "w") as data_file:
                json.dump(data, data_file, indent=4)

    def __str__(self):
        return f"{self.name}: {self.quantity} Kg"
