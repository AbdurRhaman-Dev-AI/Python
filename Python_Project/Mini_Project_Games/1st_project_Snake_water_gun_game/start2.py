import random

computer = random.choice([-1, 0, 1])
user = input("Enter your choice : ")

list = {"s": 1, "w": -1, "g": 0}
you = list[user]
reverselist = {0: "gun", -1: "water", 1: "snake"}

print("Computer chose ", reverselist[computer])
print("Computer chose ", reverselist[you])


if (computer == you):
    print("You both chose the same\nit's a drow")
else:
    # if (computer == (1, -1, 0) and you == (-1, 0, 1)):
    if ((computer == 1 and you == -1) or (computer == -1 and you == 0) or (computer == 0 and you == 1)):
        print("You Lose")
    else:
        print("You Win")