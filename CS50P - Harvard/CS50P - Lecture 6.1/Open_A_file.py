# # in this code we are going to learn how to create a file by using open function and write someting on the txt file

name = input("what is your name? ")
file = open("Names.txt", "w")
file.write(name)
file.close()