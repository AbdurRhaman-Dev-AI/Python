#_______List____Method________
# list is mutable we can change thare content and value


# name = ["Cat", "Dog", "Ant", "Bird", "Fish"]

# print(name)
# #in hera we use append method to add item in the end of the list
# name.append("Horse")
# name.append("Owl")
# name.append("Lama")
# print(name)

# in hera we use the sort method to sort the list like low to high 
# l1 = [1, 34, 62, 3, 92, 6, 11]
# l1.sort()
# print(l1)

#in hear we use the revrse method to reverst the line end to start or start to just flip the row(self, *args, **kwargs):
# OK = [ 63, 55, 99, 33, 20, 0, 2]
# OK.reverse()
# print(OK)

#in here we use the index method to find the index of the item
# name = ["Cat", "Dog", "Ant", "Bird", "Fish"]
# # print(name.index("Dog"))
# print(name.index("Fish"))

#in hear we use the insert method to insert the item in the list at any part of the list
# hi = [3, 444, 55]
# hi.insert(1, 22)
# hi.insert(3, 999)
# print(hi)



# Now we see the pop method

ok = [15, 32, 35, 74, 25]
# ok.pop(3)
# print(ok.pop(3))
hi = ok.pop(3)
print(hi)
print(ok)