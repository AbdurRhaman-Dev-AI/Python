# writing a program to get accace to a file if the user name is exist on the list

list = ["Marin", "Joy", "Harry", "Abdur Rhaman", "Rafi", "Raka"]

user_name = input("Enter your user name : ")

if (user_name in list):
    print("Welcome", user_name, "permission granted")

else:
    print("Permission denied")
    print(user_name, "You don't have permission to access this file")
