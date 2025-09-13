# # in this code we are going to use name.append(line.strip()) to append the
# # name in the list and use strip function to remove the new line character
# # and use for name in sorted(names): to sort the list like A to Z

names = []

with open("Names.txt")as file:
    for line in file:
        names.append(line.strip())


for name in sorted(names):
    print(f"Hello, {name}")