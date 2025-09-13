# # in this code we are using rstrip function to remove the new line character
# # and we use for line in file: to read the file
# # this function make the code more simple and smaller

with open("Names.txt", "r") as file:
    for line in file:
        print("hello", line.rstrip())