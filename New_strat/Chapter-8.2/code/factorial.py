def factorial(n):
    if n==1: return 1
    return n * factorial(n - 1)

print (factorial(6))



def fac(n):
    if(n == 1 or n == 0): return 1
    return n * fac(n - 1)

n = int(input("Enter a number: "))
print(fac(n))