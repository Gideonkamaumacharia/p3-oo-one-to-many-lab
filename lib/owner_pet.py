class Pet:
    PET_TYPES = ['dog', 'cat', 'rodent', 'bird', 'reptile', 'exotic']
    all = []

    def __init__(self, name, pet_type, owner=None):
        if not isinstance(name, str):
            raise Exception("Pet name must be a string!")
        if pet_type not in Pet.PET_TYPES:
            raise Exception("Invalid pet type!")
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        Pet.all.append(self)

    def __repr__(self):
        return f"Pet(name='{self.name}', type='{self.pet_type}')"



class Owner:
    def __init__(self, name):
        if not isinstance(name, str):
            raise Exception("Owner name must be a string!")
        self.name = name

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("Invalid pet type!")
        pet.owner = self

    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]

    def get_sorted_pets(self):
        owner_pets = [pet for pet in Pet.all if pet.owner == self]
        return sorted(owner_pets, key=lambda x: x.name)
