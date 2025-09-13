# # in this code we are using sorted function to sort the list by alphabet
#  # like it The starting latter is Capital that will sort in Capital list and
#  # if the starting latter is small it will sort in small list like a-z
# # and use reverse=True to sort the list in reverse order


names = []

with open("Names.txt") as file:
    for line in file:
        names.append(line.strip())

for name in sorted(names, reverse=True):
    print(f"Hello, {name}")