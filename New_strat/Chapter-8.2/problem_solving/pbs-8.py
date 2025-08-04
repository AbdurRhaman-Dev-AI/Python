# # write a program using function that will print the multiplication tavle of given number
# # formula (f"{n} * {i} = {n * i}")

def multi(n):
    if (n == 0): return
    for i in range(1, 11):
        print(f"{n} * {i} = {n * i}")

n = (int(input("Enter a number: ")))
multi(n)