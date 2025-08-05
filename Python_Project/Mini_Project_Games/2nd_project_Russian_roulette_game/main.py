import random
user = (int(input("Now you fire the Gun: ")))
computer = random.choice([1, 2, 3])

bullet = random.choice([1, 2, 3])

if (user == bullet and computer == bullet):
    print("You both died")
    if (user == bullet):
        print("You died\n Computer Win")
    elif (computer == bullet):
        print("You Win\n Computer died")
else:
    print("You both survived")