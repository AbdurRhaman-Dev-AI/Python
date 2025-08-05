import random
def game():
    user = int(input("Now you fire 🔫 the Gun : "))
    computer = random.choice([1, 2, 3])
    bullet = random.choice([1, 2, 3])
    if (user == bullet and computer == bullet):
        print("You both chose the bullet!\n You both died! ☠️ ")
    elif (user == bullet):
        print("You chose the bullet. You died! ☠️\nComputer wins! 🤖🎉")
    elif (computer == bullet):
        print("Computer chose the bullet. Computer died!🤖☠️\nYou win! 🎉")
    else:
        print("You both survived 🎉🎉. It's a tie!")
    print(f"Computer chose: {computer}")
    print(f"Bullet was in chamber: {bullet}")

game()