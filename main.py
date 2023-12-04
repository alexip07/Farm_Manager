from classes.crops import Crop
from classes.animals import Animal
from classes.management import FarmManagement
from classes.resources import Resource

# Create objects where we provide the type, name, quantity, and, if applicable, a health status
# -> Animals
cow = Animal("Cow", "Bovine", 100, "cow no. 24, injured leg")
pig = Animal("Pig", "Porcine", 50, "pig no. 10, missing")
sheep = Animal("Sheep", "Ovine", 50)
bull = Animal("Bull", "Bovine", 24)

# -> Crops
wheat = Crop("Wheat", "Cereals", 500)
rye = Crop("Rye", "Cereals", 250)

# -> Raw Materials
flour = Resource("Flour", 25)

# Create the object responsible for farm management
farm_management = FarmManagement()

# Add the objects created above to the farm and save them in a JSON file
# -> Animals
sheep.add_to_farm(farm_management)
bull.add_to_farm(farm_management)
cow.add_to_farm(farm_management)
pig.add_to_farm(farm_management)

# -> Crops
wheat.add_to_farm(farm_management)
rye.add_to_farm(farm_management)

# -> Raw Materials
flour.save_raw_materials(farm_management)

# These methods are used to save a feeding and watering history
# -> Animals
cow.feed("Feed")
pig.feed("Forage")
cow.feed("Hay")

# -> Crops
wheat.water("Ammonium nitrate")
rye.water("Ammonium nitrate")

# Method specific to the Animal class where we modify the health status of an animal

# cow.set_health("leg is fine")
# pig.set_health("found")
# pig.set_health("")
# cow.set_health("")
wheat.set_crop_state("mosaic disease")

# Methods used to add or subtract quantity
# -> Animals
cow.add_quantity(100)
cow.add_quantity(50)
cow.reduce_quantity(27)
bull.add_quantity(44)

# -> Crops
wheat.add_crop_quantity(27)
rye.reduce_crop_quantity(14)

# -> Raw Materials
flour.add_raw_material_quantity(13)

# Display the current state of the farm
farm_management.display_farm_state()

# Display the history of crops and animals
farm_management.read_animal_history()
farm_management.read_crop_history()
