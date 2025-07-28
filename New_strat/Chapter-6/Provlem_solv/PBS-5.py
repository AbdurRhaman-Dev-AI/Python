# now eritting a program to find the given user name is less then 3 charecters or more then 18 charecters

name = (input("Enter your name : "))

if (len(name) < 2 or len(name) >= 18):
    print("your name is invalid")
    print("and your name conten ", len(name), " charecters")

else:
    print("your name is valid")
    print("and your name conten ", len(name), " charecters")

print("Thank you for using this program")
print("this is the end of the program")