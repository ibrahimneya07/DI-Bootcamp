users=input("saisir un mot\n")
dict={}
for i,j in enumerate(users):
    if j not in dict:
        dict[j]=[]

    dict[j].append(i)
print(dict)