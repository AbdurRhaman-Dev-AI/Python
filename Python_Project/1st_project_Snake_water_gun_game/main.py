import random  # # we have to import the random module to give random numbers to the computer

Computer = random.choice([0, 1, 2])
User = (input("Enter your choice : "))

yourDictonary = {"g": 0, "w": 1, "s":  2}
reverseDict = {2: "snake", 1: "water", 0: "gun"}

You = yourDictonary[User]

if (Computer == You):
    print("Draw")
else:
    if (Computer == 0 and You == 2):
        print("You Lose")
    if (Computer == 1 and You == 2):
        print("You Lose")
    if (Computer == 1 and You == 0):
        print("You Lose")
    else:
        print("You Win")

print(f"You chose {reverseDict[You]}\nComputer chose {reverseDict[Computer]}")
