import random

computer = random.choice([-1, 0, 1])
user = input("Enter your choice : ")

list = {"s": 1, "w": -1, "g": 0}
you = list[user]

print("Computer chose ", computer)

if (computer == you):
    print("You both chose the same\nit's a drow")
else:
    if (computer == 1 and you == -1):
        print("You Lose")
    elif (computer == -1 and you == 0):
        print("You Lose")
    elif (computer == 0 and you == 1):
        print("You Lose")
    else:
        print("You Win")