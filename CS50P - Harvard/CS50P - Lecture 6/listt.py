# # in this code we use sorted() function to list the names in small to large name


names = []

with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())


for name in sorted(names):
    print(f"hello, {name}")