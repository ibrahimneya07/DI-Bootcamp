sandwich_orders=["Tuna sandwich","Avocado sandwich","Egg sandwich","Sabih sandwich","Pastrami sandwich"]
print("le charcuterie n'a plus de pastrami")
while "Pastrami sandwich" in sandwich_orders:
    sandwich_orders.remove("Pastrami sandwich")
if "Pastrami sandwich"*3 in sandwich_orders:
    print("pastrami sandwich")

finished_sandwiches=[]
for i in sandwich_orders:
    finished_sandwiches.append(i)
for i in finished_sandwiches:
    print("I made your "+i)
print(finished_sandwiches)