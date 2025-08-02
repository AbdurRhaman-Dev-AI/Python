# list = ["apple", "banana", "cherry", 4, 5]
# print(type(list))

# tuple = ("cat", "dog", "tom")
# print(type(tuple))

# set = {
#     "apple",
#     "banana",
#     "cherry"
# }
# print(type(set))

# now list with for loop
LIST = ["Cat", "Dog", "Goat"]

# for i in range(len(LIST)):
#     print(LIST[i])
print(type(LIST))


# som the same list with while loop

# i = 0
# while (i < len(LIST)):
#     print(LIST[i])
#     i = i + 1
print(type(LIST))

# # now with tuple with for loop

TUP = ("1", "FUK-Q", "Hell nahh", False)

# for i in range(len(TUP)):
#     print(TUP[i])
print(type(TUP))


# # now the same tuple with while loop

# i = 0
# while (i < (len(TUP))):
#     print(TUP[i])
#     i = i + 1
# print(type(TUP))


# now set with for loop

# SET = {
#     "apple",
#     "banana",
#     "cherry"
# }
# x = list(SET) # # just remember this you have to first convert set to list or you get error like 100 time just like now
# print(type(x))
# for i in range(len(x)):
#     print(x[i])


# # now try the same code same method but using while loop

set = {
    "Egg",
    "Milk",
    "Butter"
}
print("And this is the befor convert set to list", type(set))
x = list(set)
print("Now its convert set to list", type(x))

i = 0
while (i < len(x)):
    print(x[i])
    i = i + 1