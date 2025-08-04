# # ok now try to print a pattern by help of recurtion

def pattern(n):
    if (n == 0):
        return
    print("*" * n)
    pattern(n - 1)

n = (int(input("Enter the value : ")))
pattern(n)