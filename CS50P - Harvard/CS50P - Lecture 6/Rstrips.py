# In this code I use rstrip() function to remove the new line 
# from the names in the text file


with open("names.txt", "r") as file:
    for line in file:
        print("hello, ", line.rstrip())