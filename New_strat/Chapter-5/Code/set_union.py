s1 = {1, 5, 75}
s2 = {8,44, 50, 5, 1}

print(type(s1))
print(type(s2))

print(s1.union(s2))  # the unoion method just comvine s1 and s2 and take all the values to make one set or list

print(s1.intersection(s2))  #  this intersection method just return only thod values wich one is common in 2 sets

print(s1 - s2)  # the output is 75 couse 1 and 5 is comon and they cut thare value and 75 is left thas why s1 - s2 = 75

