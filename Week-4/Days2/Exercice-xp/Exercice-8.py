list_garnitures=[];
while True:
    garnitures=str(input("saisir une serie de garnitures de pizza\n"));
    if garnitures =="quitter":
        break
    else:
        print("J'ajouterez cette garniture à leur pizza.");
        list_garnitures.append(garnitures);
taille=len(list_garnitures)
print("voici les granitures sur la pizza")
for i in list_garnitures:
    print(i)
prix=(12.5)*taille
print("le prix total est: "+str(prix));    
    