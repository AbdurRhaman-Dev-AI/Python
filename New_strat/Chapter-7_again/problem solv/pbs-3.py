# # write a program that will varifiy the user if the naame is mantion in list

# list = ["Marin", "Harry", "Rohan", "Rhaman"]

# user = (input("Enter your name: ")).lower()

# for name in list:
#     if user == name.lower():
#         print("You are invited")
#         break
# else:
#     print("You are not invited")


# # 

listed = ["Mark", "Hanry", "Tanim", "Marin"]

user = input("Enter your name: ").lower()

i = 0

while (i < len(listed)):
    if user == listed[i].lower():
        print("your are invited")
        break
    i = i + 1
else:
    print("You are not invited")