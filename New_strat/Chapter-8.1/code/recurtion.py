# # factorial
# # factorial(n) = n *factorial(n-1)

def fatorial(n):
    if (n == 1 or n == 0):
        return 1
    return n * fatorial(n - 1)

n = (int(input("Enter the value : ")))
print(fatorial(n))