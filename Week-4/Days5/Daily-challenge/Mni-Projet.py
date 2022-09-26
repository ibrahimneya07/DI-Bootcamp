from cgitb import text

mot=input("Saisir une séquence de mots séparés par des virgules\n")
mot=mot.split(",")
mot.sort()
print(mot)