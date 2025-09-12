# # in this code we are going to learn how to take input from the user by
# # using for loop and append fuction

name = []

for _ in range(3):
    name.append(input("What is your name? "))


for name in (name):
    print(f"hello {name}")