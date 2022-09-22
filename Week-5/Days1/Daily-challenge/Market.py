
class Farm:
    def __init__(self,name,animals):
        self.name=name
        self.animals=animals
        print(f"{self.name}'s farm")
# Meethde ajout
    def add_animal(self,name,n):
        print(f"{name}:{n}")

# Method information

    def get_info(self):
        return'\tE-I-E-I-0!'

# Method type d'animal

    def get_animal_types(self):
        print(self.animals)

# Method get_short_info

    def get_short_info(self):
        print("Macdonalas far has",end=" ")
        self.get_animal_types()

# object
macdonald = Farm("McDonald","['cow','goat',sheet]")
macdonald.add_animal('cow',5)
macdonald.add_animal('sheep',n=2)
macdonald.add_animal('goat',n=12)
print(macdonald.get_short_info())
macdonald.get_animal_types()
macdonald.get_short_info()

# Method