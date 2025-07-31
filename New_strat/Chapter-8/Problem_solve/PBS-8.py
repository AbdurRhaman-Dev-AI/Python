# # write a program that will print the multiplication table of a given number using function


def multiply(n):
    for i in range(1, 11):
        print(f"{n} * {i} = {n * i}")

n = (int(input("Enter the number : ")))

multiply(n)