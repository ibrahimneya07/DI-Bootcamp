from math import degrees
import random

def get_random_temp(saison):
    saison=random.randint(-10,40)
    if saison=="hiver":
        print("on n'est en Hiver")
    if saison=="printemps":
        print("on n'est au printemps")
    


print("---------function main----------")
def main():
    saison=input("Saisir la saison\n")
    degre=get_random_temp(saison)
    print(f"la temperature actuelle est de {degre} °Celsius")

    if degre<0:
        print("Brrr, c'est glacial ! Portez des couches supplémentaires aujourd'hui")
    elif 0<degre<16:
        print("Assez froid ! N'oubliez pas votre manteau")
    elif 16<degre<23:
        print("Un peu de clime")
    elif 24<degre<32:
       print( "Chaud")
    elif 32<degre<40:
        print("tres tres chaud")
main();