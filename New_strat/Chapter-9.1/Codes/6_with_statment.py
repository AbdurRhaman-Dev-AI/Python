# # hear we use with statment to simplify the code

# f = open("file.txt")

# with f:
#     print(f.read())


# # now i will show make it more efficient

with open("file.txt") as f:
    print(f.read())