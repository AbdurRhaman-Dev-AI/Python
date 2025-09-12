# # in this core we are using sorted function to sort the list by alphabet like it The starting latter is Capital that will sort in Capital list and if the starting latter is small it will sort in small list like a-z

name = []

for _ in range(3):
    name.append(input("What is your name? "))

for name in sorted(name):
    print(f"hello {name}")