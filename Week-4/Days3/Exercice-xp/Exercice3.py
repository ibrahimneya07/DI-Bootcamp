
from distutils.command.clean import clean


brand={
    'name': 'Zara' ,
    'creation_date': 1975,
    'creator_name': 'Amancio, Ortega, Gaona' ,
    'type_of_clothes':[ 'men', 'women', 'children', 'home'] ,
    'international_competitors': ['Gap', 'H&M', 'Benetton'] ,
    'number_stores': 7000 ,
    'major_color': {
        'France': 'blue', 
        'Spain': 'red', 
        'US':[ 'pink', 'green']
    }
        
}
brand["number_stores"]=2
print("les clients de Zaras sont:")
for i in brand['type_of_clothes']:
    print(i)

brand['country_creation']='marron'
if 'international_competitors' in brand:
        brand['international_competitors'].append("Desigual")

del brand['creation_date']
print("le dernier elements de international_competitors est: "+brand['international_competitors'][3])
print("les couleurs de vetements aus Etats Unis sont: ")
for i in brand['major_color']['US']:
    print(i)
print("Notre dictionnaire à: "+str(len(brand))+" clé")
print("les clés du dictionnaire sont:")
for i in brand:
    print(i)


more_on_zara={
    'creation_date': 1975 ,
    'number_stores': 10000
}

brand.update(more_on_zara)
print("le numbers stores est: "+str(brand['number_stores']))
# le numbers stores vient de passer de 7000 à 10000