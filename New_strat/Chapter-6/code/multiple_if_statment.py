#  write a program content multiple if statment

a = int(input("Enter your age : "))

# first if statment
if (a % 2 == 0):
    print("your age is even")
#  end of first if statment

# second if statment
if (a >= 18):
    print("your are above the age of consernt")
#  end of second if statment

elif (a < 18):
    print("your age is invalid")

else:
    print("your age is not valid")

print("this is the end of the program")