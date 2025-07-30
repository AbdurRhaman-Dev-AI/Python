# now write a program that will print items of the tuple using loops

# ok now try with for loops

# tuple = ("Fire", "Water", "Air", "Earth")
# print(type(tuple))

# for i in tuple:
#     print(i)

# # ok now write the same program using while loop

Tuple = (
    "Lava",
    "Ice",
    "Watet",
    "Sand",
)
print("the type is ", type(Tuple))

i = 0
while (i < len(Tuple)):
    print(Tuple[i])
    i = i + 1