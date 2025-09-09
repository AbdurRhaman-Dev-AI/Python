name = input("Enter your name: ")

# file = open("names.txt", "w")  # # w == write mode
file = open("names.txt", "a")  # a == append mode
file.write(f"{name}\n")
file.close()