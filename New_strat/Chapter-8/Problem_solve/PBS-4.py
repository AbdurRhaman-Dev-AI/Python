"""
sum(1) = 1 
sum(2) = 1 + 2 = 3 
sum(3) = 1 + 2 + 3 = 6
sum(4) = 1 + 2 + 3 + 4 = 10
sum(5) = 1 + 2 + 3 + 4 + 5 = 15
sum(6) = 1 + 2 + 3 + 4 + 5 + 6 = 21
sum(n) = 1 + 2 + 3 + 4 + 5 + 6 + ... + n
"""
# # sum(n) = sum(n-1) + n

def sum(n):
    if (n == 1):
        return 1
    return sum(n - 1) + n

n = (int(input("Enter the number: ")))
print(sum(n))