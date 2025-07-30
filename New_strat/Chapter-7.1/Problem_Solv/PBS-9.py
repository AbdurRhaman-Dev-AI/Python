# # write a program that will print a multiplication table of given number in reverse order using for loop

# n = (int(input("Enter the number : ")))

# for i in range(1, 11):
#     print(f"{n} * {11-i} = {n*(11-i)}")


# now try with while loop

N = (int(input("Enter the number : ")))

i = 10
while (i >= 1):
    print(f"{i} * {N} = {i * N}")
    i = i - 1