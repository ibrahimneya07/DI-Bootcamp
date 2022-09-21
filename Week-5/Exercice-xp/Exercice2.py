class Dog():
    def __init__(self,name,height):
        self.name=name
        self.height=height

    def bark(self):
        print(f"{self.name} va woof!")

    def jump(self):
        print(f"{self.name} saute {self.height*2} cm de haut!")


davids_dog=Dog("Rex",50)
print("-----------le nom de son chien-----------")
print(davids_dog.name)
print("-----------la taille de son chien-----------")
print(davids_dog.height)
print("-------------appelle de la fonction bark-----------")
davids_dog.bark()
print("-------------appelle de la fonction jump-----------")
davids_dog.jump()
sarahs_dog=Dog("Teacup",20)
print("-----------le nom de son chien-----------")
print(sarahs_dog.name)
print("-----------la taille de son chien-----------")
print(sarahs_dog.height)
print("-------------appelle de la fonction bark-----------")
sarahs_dog.bark()
print("-------------appelle de la fonction jump-----------")
sarahs_dog.jump()

print("----------------le grand chien----------------")
if davids_dog.height>sarahs_dog.height:
    print(f"le plus grand chien est {davids_dog.name}.")
else:
    print(f"le plus grand chien est {sarahs_dog.name}.")
