# # in this code we are going to learn how to take input from the user by
# # using for loop and append fuction and use "\n" new line fuction to list in new line

name = input("What is your name? ")

file = open("Names.txt", "a")
# file.write(name + "\n")
file.write(f"{name}\n")
file.close()