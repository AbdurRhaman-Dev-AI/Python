import random

user = (int(input("Enter your choice : ")))
computer = random.choice([1, 2, 3])

print("Computer chose ", computer)

def game():
    if (computer == user):
        print("it's a drow\n you both chose the same")
    elif (computer == 1 and user == 3):
        print("You Win")
    elif (computer == 2 and user == 1):
        print("You Win")
    else:
        print("You lose")

    return

game()