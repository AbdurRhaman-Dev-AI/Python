#  in this code if first if statment is true the it will print the first statment,
# if the first if statment is false it will print the else statment 

a = int(input("Enter your age : "))

#  this is if statment
if (a >= 21):
    print("you can drink alcohol and ride a car")
    print("this is valid age")

# this is elif statment
elif (a < 0):
    print("this is invalid age")

# this is elif statment
elif (a == 0):
    print("this is not a valid age")

# this is else statment
else:
    print("no you age is less then 21 you can't drint or deive")

print("this is the end of the program")
