# # in this code i open the file in read mode and use readlines function
# # and use strip function to remove the new line character
# # and i can use end="" to remove the new line character same as the strip function

with open("Names.txt", "r") as file:
    lines = file.readlines()

for line in lines:
    # print("hello "+line, end="")
    print("hello "+line.strip())