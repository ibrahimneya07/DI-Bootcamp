from ast import walk


class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'
class Siamese(Cat):
    def sing(self, sounds):
        return f'{sounds}'
Bengal=Bengal("Roger",4)
Chartreux=Chartreux("Milan",5)
Siamese=Siamese("Smith",6)
all_cats=[Bengal,Chartreux,Siamese]
sara_pets=Pets(all_cats)
sara_pets.walk()
