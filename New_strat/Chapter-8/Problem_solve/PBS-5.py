# # write a program that will print a pattern of given number using help of function

def pattern(n):
    if(n == 0):
        return
    print("*" * n)
    pattern(n - 1)

pattern(5)