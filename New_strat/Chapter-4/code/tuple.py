#______Tuple_is___immutable______we can't change the value or list

# A = (1, 2, 5, 9) # this is a tuple
# A = (1) # if we make this with only one item or number them it will cald (int) as intejer value or type
#A= (1,) # tis is the way we can make a tuple with only one item
# print(type(A))
# a = (1, 45, 324, 3424, False, "rohan", "marin")
# a[0] = 999 # using this mathod we cant change taple value taple is immutable
# print(type(a))

# no = a.count(45) # in hear we are using the count  to count the number whare is the value we gave
# no = a.count(2) # if we give wrong value it will return 0 cous the value dosent exit in this tuple
# print(no)

# bb = a.index("marin") # in hear we are using the index method to find the index of the item
# bb = a.index("Gojo") # in hear we are using the index method and give wrong value to find the index of the item it will return an error
# print(bb)

# z = (1, 2, 3)
# repeated = z * 3 # in hear we using the repeated  and give  *3 it means this tuple will be repeated for 3 times
# print(repeated)

x = (1, 2, 3)
print(2 in x) # hear we can chack the value is exit or not in the truple list
print(9 in x) # and if we try to find wrong valie then it will give false to us
print(len(x)) # we use len to find the length of the tuple
a, b, c = x # in hear we are using the tuple unpacking to assign the value of the tuple to the variables
print(a, b, c)