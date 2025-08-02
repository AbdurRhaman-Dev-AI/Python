n = (int(input("Enter a number : ")))

for i in range(1, n+1):
    if (i == 1) or (i == n):
        print("x" * (n), end="")
    else:
        print("x", end="")
        print(" " * (n - 2),end="")
        print("x", end="")
    print("")