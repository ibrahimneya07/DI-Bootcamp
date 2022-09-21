class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

# liste d'objets
list=[]
list.append(Cat("Meawous",3))
list.append(Cat("Oggi",2))
list.append(Cat("Tom",4))

for objet in list:
    age=0
    if objet.age>age:
        age=objet.age
print(f"le chat le plus ancien est {objet.name} et a {objet.age}ans.")
    