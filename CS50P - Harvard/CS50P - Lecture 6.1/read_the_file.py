# # in this code i open the file in read mode and use readlines function
# # and use strip function to remove the new line character

with open("Names.txt", "r") as file:
    lines = file.readlines()

for line in lines:
    print("hello "+line.strip())