import random

user = (input("Now you shoot : "))
computer = random.choice([1, 2, 3])

bullet = random.choice([1, 2, 3])

if (user == bullet and computer == bullet):
    print("You both died")
elif (user == bullet):
    print("You died\n Computer Win")
elif (computer == bullet):
    print("You win\n Computer died")
else:
    print("You both survived")

print("Computer chose :", computer)
print("Bullet was in chamber :", bullet) 