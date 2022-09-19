import random

def generate():
    numero=int(input("veuillez saisir un nombre entre 1 et 100\n"))
    if numero<1 and numero>100:
        numero=input("veuillez saisir un nombre entre 1 et 100\n")
    elif 1<numero<100:
        generer=random.randint(1,100)
        if numero==generer:
            print("le numero generer est" +str(generer))
            print("Win, les deux nombre sont les meme")
        elif numero!=generer:
            print("le numero generer est " + str(generer))
            print("les deux nombres sont differents")

generate()