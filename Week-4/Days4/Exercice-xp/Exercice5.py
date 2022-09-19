# fonction principal
print("-----------fonction principal----------------")
def make_shirt(taille,message):
    print(f"The size of the shirt is {taille} and is the text is {message}")
make_shirt(45,"GUCCI")

print("------------fonction modifier----------------")
def make_shirt(taille="grandes",message="J'aime python"):
    print(f"The size of the shirt is {taille} and is the text is {message}")
make_shirt()

print("----------large shirt with a deffault message---------")

def make_shirt(taille,message="J'aime python"):
    print(f"The size of the shirt is {taille} and is the text is {message}")
make_shirt("large shirt")


print("----------medium shirt with a deffault message---------")

def make_shirt(taille,message="J'aime python"):
    print(f"The size of the shirt is {taille} and is the text is {message}")
make_shirt("medium shirt")

print("----------a shirt of any size with a different message---------")

def make_shirt(taille,message):
    print(f"The size of the shirt is {taille} and is the text is {message}")
taille=input("Faites une chemise de n'importe quelle taille\n")
message=input("saisir un message a imprimer sur votre chemise\n")
make_shirt(taille,message)

print("----------a shirt of any size with a different message---------")

def make_shirt(taille,message):
    print(f"The size of the shirt is {taille} and is the text is {message}")
taille=input("Faites une chemise de n'importe quelle taille\n")
message=input("saisir un message a imprimer sur votre chemise\n")
make_shirt(taille,message)
