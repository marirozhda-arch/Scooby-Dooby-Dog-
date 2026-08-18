from pet import Pet
from product import Product
from console_helper import *

global_pet_id = 0

def get_next_pet_id() -> int:
    global global_pet_id

    global_pet_id += 1

    return global_pet_id

def input_product_data() -> Pet:
    icon = input_str()
    name = input_str()
    breed = input_int()
    diseases = input_str()
    health_status = input_int()
    story = input_str()
    age = input_date()
    color = list(input_int())
    character = list(input_int())

    return Pet(
        icon=icon,
        name=name,
        breed=breed,
        diseases=diseases,
        health_status=health_status,
        story=story,
        age=age,
        color=color,
        character=character,
    )
    
def get_pet_by_id(pets: list[Pet], search_id: int) -> Pet | None:
    for pet in pets:
        if pet.id == search_id:
            return pet
        
    return None

def add_pet_to_list(pets: list[Pet], pet: Pet):
    pets.append(pet)

def update_pet_by_id(pets: list[Pet], pet: Pet) -> bool:
    find_pet = get_pet_by_id(pets, pet.id)

    if find_pet == None:
        return False

    find_pet.icon = pet.icon
    find_pet.name = pet.name
    find_pet.breed = pet.breed
    find_pet.diseases = pet.diseases
    find_pet.health_status = pet.health_status
    find_pet.story = pet.story
    find_pet.age = pet.age
    find_pet.color = pet.color
    find_pet.character = pet.character

    return True
