class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]

    all = []

    def __init__(self, name, pet_type, owner=None):
        self.name = name
        if pet_type in self.PET_TYPES:
            self.pet_type = pet_type
        else:
            raise ValueError
        self.owner = owner
        Pet.add_pets_to_all(self)
        
    @classmethod
    def add_pets_to_all(cls, Pet):
        if Pet not in Pet.all:
            cls.all.append(Pet)

class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]
    
    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise TypeError
        pet.owner = self
    
    def get_sorted_pets(self):
        sorted_pets = sorted(self.pets(), key=lambda pet: pet.name)
        return sorted_pets
    
    def sort_pets_by_name(self):
        if not all(isinstance(pet, Pet) for pet in self.pets):
            raise Exception
        