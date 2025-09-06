import sys

# # check for errors
if len(sys.argv) < 2:
    print("Too few arguments")
elif len(sys.argv) > 2:
    print("Too many arguments")

# print the name tags
print("Hello, my name is ", sys.argv[1])