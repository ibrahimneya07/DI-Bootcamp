fruits=str(input("Saisissez vos fruits prefere\n"));
# convertir une chaine de mot en liste de mot
list_mot=fruits.split();
print(list_mot);

entre=str(input("Entrer le nom de n'importe quelle fruit\n"));
if entre in list_mot:
    print(" Vous avez choisi l'un de vos fruits préférés ! Prendre plaisir!");
else:
    print("Vous avez choisi un nouveau fruit. J'espère que tu apprécies");