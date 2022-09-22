from Exercice2 import Dog 

class PetDog(Dog):
    def __init__(self, name, age, weight,trained=False):
        self.trained=trained
        super().__init__(name, age, weight)
    def train(self): 
        self.bark()
        self.trained=True
    def play(self,*args):
        print(f"{args} jouent ensemble")


list1=Dog("berger",5,50)
list2=Dog("milou",6,45)
list3=Dog("Rex",7,40)