# # write a program that give the sum of the given number
# # sum = 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + n
n = (int(input("Enter a number : ")))
i = 0
sum = 0
while (i <= n):
    sum = sum + i  # hear we are adding i to the sum
    i = i + 1
print(sum)  # and we make sure print is not inside the loop indenttation or it will give wrong answer
