# convertion de deux listes en dictionnaire
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
my_dict={item for item in zip (keys,values)}
print(my_dict)