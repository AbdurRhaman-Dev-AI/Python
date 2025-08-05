import random
# # we import the random module to get random number
user = (input("Now you fire the Gun : "))
Computer = random.choice([1, 2, 3])   # # hear we give the computer to choice the random number it want

bullet = random.choice([1, 2, 3])   # # and hear is the bullet chamber and we give it random number to change bullet chembers how it want

# # in hear we write the logical condition to execute the program
if (user == bullet and Computer == bullet):
    print("You both died")
elif (user == bullet):
    print("You died \n Computer Win")
elif (Computer == bullet):
    print("You Win \n Computer died")
else:
    print("You both survived")

# # now lets print Computer choices what and Wich chamber bullet was in

print("Computer chose :", Computer)
print("Bullet was in chamber :", bullet)