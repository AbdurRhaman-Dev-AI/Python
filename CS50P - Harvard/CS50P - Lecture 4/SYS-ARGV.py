import sys

# print("Hello, my name is", sys.argv[1])


# # Error Handling

# # try/except
# try:
#     print("Hello, my name is ", sys.argv[1])
# except IndexError:
#     print("Hello, my name is Guest")

# # if statement
if len(sys.argv) < 2:
    print("Too few arguments")
elif len(sys.argv) > 2:
    print("Too many arguments")
else:
    print("Hello, my name is ", sys.argv[1])
