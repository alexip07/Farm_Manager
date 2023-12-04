# Farm_Manager

The main.py file can be an example of how to use the classes.

Description:
The "Farm Management" project is a simple application for managing animals, crops, and raw materials on a farm. It uses object-oriented programming (OOP) concepts to define the main classes: Resource, Animal, Crop, and FarmManagement.

Resource Class:

The Resource class is the base class for the Animal and Crop classes. A resource has a name and an associated quantity. It also has the role of creating and storing raw materials. This includes methods such as:
-> save_raw_materials to save raw materials in a JSON file
-> add_raw_material_quantity/reduce_raw_material_quantity to modify the quantity of raw materials

Animal Class:

This includes methods such as:
-> feed to feed the animal
-> set_health to update the health status
-> add_to_farm to add an animal to the current farm
-> add_quantity/reduce_quantity to modify the quantity of animals

Crop Class:

This includes methods such as:
-> water to water the plants
-> add_to_farm allows adding a crop to the current farm
-> add_crop_quantity/reduce_crop_quantity to modify the quantity of crops
-> set_crop_state to update the health status

FarmManagement Class:

The FarmManagement class manages the animals, crops, and raw materials on the current farm. It includes methods such as:
-> add_animal to add an animal to the current farm
-> add_crop to add a crop
-> add_raw_material to add a raw material
-> display_farm_state to display the current state of the farm
-> and the two history reading methods display data saved by the water/feed/set_health/set_crop_state methods

Project Structure:

-> data/: The directory containing JSON files for data storage - files will be created automatically when running the code from main.py
-> classes/: The directory containing modules for the main classes
-> main.py: The main file that uses the classes for farm management.
