class Zoo():
    def __init__(self,zoo_name,animals,name):
        self.animals=animals
        self.name=name
    
    def add_animal(self,new_animal,animals):
        if new_animal is not animals:
            animals.append(new_animal)

    def get_animals(animals):
        for i in animals:
            print(i)

    def sell_animal(self,animal_sold,animals):
        if animal_sold is animals:
            animals.clear(animal_sold)
    def sort_animals(animals):
        animals.sort()
    def get_groups():