# # now rwite a program to print the first natural numbers of n umbers using sum function

# # sum(n) = sum(n-1) + n

def sum(n):
    if (n == 1): return 1
    return sum(n-1) + n
n = (int(input("Enter a number: ")))
print(sum(n))