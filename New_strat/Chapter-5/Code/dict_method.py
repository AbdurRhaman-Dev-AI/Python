marks = {
    "Marin": 85,
    "Harry": 100,
    "Rohit": 90,
    "list": [10, 20, 30],
    0: "Harry"
}

#  print(marks.items())  # hear we use item method to print every key and item of the dictanary

#  print(marks.keys())  # hear we use the keys method to print every singel key from the dictanary

#  print(marks.values())  # hear we use the values method to print out all of thr values of the dictanary

#  hear we try the get method and try to get the value by giving key to get the value from the dictanary
# print(marks.get(0))  # and if we give the exzisting key then it will return the value
# print(marks.get("Marin"))
# print(marks.get(100)) # and if we give the wrong key to find the value it will return none

# Hear we use the clear method to fully clear the dictanary
# marks.clear()
# print(marks)  # and now ti will return a empty dictanary

# marks.update({"Marin": 100, "Harry": 69})
# marks.update({"Rohit": "39", "Raka": "55"})
# marks.update({"list": ["Daredevil", "Moon_knight", "The_Punisher"]})
# marks.update({0: "Tom"})
# print(marks)

# marks.pop(0)  # we use pop method 0 and now the 0 key and the value is removed from the dictanary
# print(marks)

marks.popitem()  # we use popitem method and now the last key and the value is removed from the dictanary
print(marks)
print(len(marks))