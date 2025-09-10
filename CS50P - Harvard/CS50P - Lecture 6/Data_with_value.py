name = input("What is your name? ")

with open("names.csv", "a") as file:
    file.write(f"{name}\n")
    file.close()