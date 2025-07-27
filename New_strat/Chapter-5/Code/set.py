# a = {} # this is a empty dictanary
# a = set() # this is a empty set

# inside a set function no repetad value is allowed like if we try {1, 2, 5, 5, 6, 5, 8, 5} and try to print it will return only {1, 2, 5, 6, 8}
#only one 5 will be printed or return value

# a = {}
# print(a, type(a))  # this is a empty dictanary

# a = set()
# print(a, type(a))  # this is a empty set


S = {1, 5, 2, 5, 3, 5, 4, 5} # hear we create a set with multiple values and four 5 but it will return only one 5
print(S)  # only one 5 will be printed couse set doesn't allow same value multiple times so it will return only one time
