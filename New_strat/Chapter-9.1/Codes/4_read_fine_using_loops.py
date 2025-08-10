# # lets try to read the files bu help of loops
# # lets try with while loop

# f = open("file_function.txt")

# line = f.readline()
# while (line != ""):
#     print(line)
#     line = f.readline()

# f.close


# # lets try with for loop

f = open("file_function.txt")

for i in f:
    print(i)

f.close