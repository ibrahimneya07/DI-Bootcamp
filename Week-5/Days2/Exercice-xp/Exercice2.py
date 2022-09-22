
class Dog:
    def __init__(self,name,age,weight):
        self.name=name
        self.age=age
        self.weight=weight
    def bark(self):
        print(f"{self.name} aboie")
    def run_speed(self):
        print(f"la vitesse de course des chiens est {self.weight/self.age*2}\n")
    def fight(self,other_dog):
        weight1=self.weight/self.age*2
        weight2=other_dog.weight/self.age*2
        if weight1>weight2:
            print(f"{self.name} est le plus fort")
        else:
            print(f"{other_dog.name} est le plus fort")


"""list1=Dog("berger",5,50)
list2=Dog("milou",6,45)
list3=Dog("Rex",7,40)
list1.fight(list2)"""