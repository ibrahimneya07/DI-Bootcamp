user=input("Saisir une chaine de caractere\n")
n=len(user)
user=list(user)
if n<2:
    print("".join(user))
else:
    j=0
    for i in range(n):
        if (user[j]!=user[i]):
            j+=1
            user[j]=user[i]
    j+=1
    user=user[:j]
print(user)
