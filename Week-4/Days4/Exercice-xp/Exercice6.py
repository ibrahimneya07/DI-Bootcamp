magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']
def show_magicians(users):
    for user in users:
        print(user)

print("---------------function mmake_great()--------------")

def make_great(users):
    for user in users:
        user=user+" the Great"
        print(user)
print("-------------la function show_magicians--------------------")
make_great(magician_names)
print("-------------la function make_great()--------------------")
show_magicians(magician_names)
