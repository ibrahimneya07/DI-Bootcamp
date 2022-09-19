# gestion d'un dictionnaire de famille
total=0
family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
for x,y in family.items():
    if y<3:
        print(f"je buillet de {x} est gratuit")
    elif 3<y<12:
        y=y*10
        total +=10
        print(f"le buillet de {x} coute 10$")
    elif y>12:
        y=y*15
        total +=15
        print(f"le buillet de {x} coute 15$")
print(f"la famille doit payer en tout {total}")
