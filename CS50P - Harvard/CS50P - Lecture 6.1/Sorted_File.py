# # in this code we open the file using with function to open and close the file automatically
# # an we use the sorted function to sort the file
# # and we use strip function to remove the new line character
# # and we can use end="" to remove the new line character same as the strip function


with open("Names.txt") as file:
    for line in sorted(file):
        # print("hello," ,line, end="")
        print("hello,", line.strip())