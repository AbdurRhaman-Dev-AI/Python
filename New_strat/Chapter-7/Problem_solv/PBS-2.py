# write a program that will great the person if the name start with "M"

#  hear we use 2 statment in the condition that if ( name.lower )this statmen will chak every letter of the input name and
#  then we give condition (name.startswith("M")) for this statment if any name start with "M" then it will be true
name = (input("Enter your name : ")).lower()

if name.lower().startswith("m"):
    print("Hello", name, "You are welcome")

else:
    print("Hello", name, " Your name is invalid")