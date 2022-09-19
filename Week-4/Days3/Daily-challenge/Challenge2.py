from multiprocessing.sharedctypes import Value


walllet=300
liste=[]
items_purchase={
    "Water":1,
    "Bread":3,
    "Tv":1000,
    "Fertilizer":20
}
for i,j in items_purchase.items():
    if walllet>j:
        walllet -=j
        liste.append(i)
print(liste)