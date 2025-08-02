# # factorial with for loop

# n1 = (int(input("Enter a number : ")))

# factorial = 1

# for i in range(1, n1 + 1):
#     factorial = factorial * i

# print(factorial)

# # now 

n2 = (int(input("Enter a number : ")))
i = 1
factorial = 1

while (i <= n2):
    factorial = factorial * i
    i = i + 1
print(factorial)