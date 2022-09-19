from multiprocessing.sharedctypes import Value
from re import I


users = ["Mickey","Minnie","Donald","Ariel","Pluto"]
# 1-------------------------------------------
dict1={}
for i in range(len(users)):
    dict1[users[i]]=i
print(dict1)        

# 2-------------------------------------------
dict2={}
for i in range(len(users)):
    dict2[i]=users[i]
print(dict2)
# 3-------------------------------------------
dict3={}
users.sort()
for i in range(len(users)):
    dict3[users[i]]=i
print(dict3)
# 4-------------------------------------------
dict3={}
users.sort()
for i in range(len(users)):
    if 'i' in users[i]:
        dict3[users[i]]=i
print(dict3)
# 5------------------------------------------
dict3={}
users.sort()
for i in range(len(users)):
    if users[i][0]=='M' or users[i][0]=='P':
        dict3[users[i]]=i
print(dict3)