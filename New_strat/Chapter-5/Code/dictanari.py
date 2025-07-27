# dictanary is a collection of key value pair and it is mutable we can change the real value and add new value on the main list

# marks = {
#     "Marin": 85,
#     "Sachin": 95,
#     "Dhoni": 100,
#     "Rohit": 90,
#     "list": [1, 2, 9]
# }

# print(marks, type(marks))  # in hear we are printing the marks from the dictanary and what is the type

# # print(marks["Marin"])  # in hear we are printing the marks of marin using the dictanary logic or sarch
# print(marks["list"])

# lets try to make a big dictanary using small dictanary


# a1 = {1: "A", 2: "B", 3: "C"}
# a2 = {4: "D", 5: "E", 6: "F"}
# a3 = {7: "G", 8: "H", 9: "I"}

# a = {**a1, **a2, **a3}
# print(a)

#___Now lets see how to update the dictanary

x1 = {100: 70, 200: 80, 300: 90, 400: 50}
x2 = {500: 100, 600: 80, 700: 60}

# x1.update(x2)  # this is how we can update the dictanary
# print(x1)

# x1.clear()  # this is how we can clear the dictanary
# print(x1)

# x1.pop(100)   # using pop we can delete the dictanary specific item or value
# print(x1)

# x1.popitem()  # using popitem we can delete the last item only last item
# print(x1)

# del x1  # using del we can delete the whole dictanary
# print(x1)  # and now the name also deleted not recoagnaized

# del x1[100]  # using del and gevind a key value we only delete the specific value not the whol dictanary
# print(x1)

# print(x1.items())  # in hear we are using the item method in dictanary to get item list
# print(x1.keys())  # hear we are using the keys method in dictanary to get keys list

# print(x1.values())  # hear we are using the values method in dictanary to get the dairect values list

# x1.update({100: 99})  # in hear we update the value of a key using update and change the specfic keys value
# print(x1)
# x1.update({100: 99, 600: 1010101})  # in hear we update the value of a key using update and change the specfic keys value and add a new key with new value
# print(x1)

# print(x1.get(100))  # hear we give the key and get the value 
# print(x1.get(800))  # hear we try with wrong value then it give us none

# print(x1.get(100))  # if we use the get method then it will return the key value and if the key dosn't exist then it will return none
# print(x1[100])  # if we use the [] braket then it will return the key balue if it exist but if the key dosent exist then it will givw an error

# x1.clear()  # this is how we can clear the dictanary
# print(x1)

#  lets try the copy() method

x1 = {100: 70, 200: 80, 300: 90, 400: 50}
x2 = x1.copy()  # this is how we can copy the dictanary
print(x2)
