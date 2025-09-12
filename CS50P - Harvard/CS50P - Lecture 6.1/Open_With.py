# # in this code we are using with function to open a file and close the file automatically

name = input("what is your name? ")
with open("Names.txt", "a") as file:
    file.write(name + "\n")