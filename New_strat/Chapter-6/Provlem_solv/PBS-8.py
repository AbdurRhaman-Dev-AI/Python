# writing a program to ditermine the post or comment or the message is abouth the person who was listed in a list

# in this program we have to know something that is 
# 💡 If you use .lower() on both sides — the input and the name you're checking-
#  you don’t need to use .upper() or .capitalize() or other functions at all.


l1 = "Abdur Rhaman"
l2 = "Rafi"
l3 = "Raka"
l4 = "Joy"
l5 = "Harry"
l6 = "Marin"


message = input("Enter your message : "). lower()

if (l1.lower() in message):
    print("yes this is a post about", l1)

elif (l2.lower() in message):
    print("yes this is a post about", l2)

elif (l3.lower() in message):
    print("yes this is a post about", l3)

elif (l4.lower() in message):
    print("yes this is a post about", l4)

elif (l5.lower() in message):
    print("yes this is a post about", l5)

elif (l6.lower() in message):
    print("yes this is a post about", l6)
else:
    print("no this is not a post about", l1, l2, l3, l4, l5, l6, "them")

print("Thank you for using this program")
print("this is the end of the program")