number=int(input("Saisir un nombre\n"))
taille=int(input("Saisir une taille\n"))
mutiple=[]
for i in range(1,taille+1):
    reponse=i*number;
    mutiple.append(reponse)
print(mutiple)