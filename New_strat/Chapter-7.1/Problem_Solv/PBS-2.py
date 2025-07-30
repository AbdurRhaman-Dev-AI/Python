# # write a program that will give permition to the user if user name start with "M"

name = (input("Enter your name : ")).lower()

if name.lower().startswith("m"):
    print("Hello", name, "Your permition is granted")
else:
    print("Hello", name, "Your permition is not granted")