# # hear we are gonna use readlines function
# # and it will read the file line by line and store it in a list

# f = open("file_function.txt", "r")

# lines = f.readlines()
# print(lines)
# print(type(lines))
# f.close()


# # and hear we are gonna use readline function
# # and it will read the fine lene by line how many line you give it to read

f = open("file_function.txt", "r")
line1 = f.readline()
print(line1)
print(type(line1))

line2 = f.readline()
print(line2)
print(type(line2))

line3 = f.readline()
print(line3)
print(type(line3))

line4 = f.readline()
print(line4)
print(type(line4))

line5 = f.readline()
print(line5)
print(type(line5))

line6 = f.readline()
print(line6)
print(type(line6))

line7 = f.readline()
print(line7 == "")
print(type(line7))

line8 = f.readline()
print(line8 == "")


f.close()