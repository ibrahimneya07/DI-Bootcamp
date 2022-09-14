saisi=input("saisir une chaine de 10 charatère\n");
if len(str(saisi))<10:
    print("Chaine pas assez longue");
elif len(str(saisi))>10:
    print("Chaine trop longue");    

print(str(saisi)[0]);
print(str(saisi)[9]);

for i in range(len(str(saisi))):
        print(str(saisi)[i]);