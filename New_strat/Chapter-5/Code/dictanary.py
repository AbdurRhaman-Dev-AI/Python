#  we use dicsanary to store the data and get the data so fast like it will find data using the key and it only look for thr key we give
# thats why we use dictanary its fast and efficient

marks = {
    "Marin": 85,
    "Harry": 100,
    "Rohit": 90,
    "list": [10, 20, 30]
}

# print(marks, type(marks))  # hear ue use the type method to know the type of the dictanary
print(marks["Rohit"])  # hear we give the key and get the marks of students

print(marks["Marin"])

a = marks["list"]  # hear we insert the list key to the a variable and we can access every list items by placing the index number

print(a)
print(a[0])  # see thst how we can access any list item and just print any item we want
print(a[1])
print(a[2])