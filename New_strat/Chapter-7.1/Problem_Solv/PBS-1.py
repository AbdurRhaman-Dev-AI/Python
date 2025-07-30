# # write a program to pring the given numbers multiplication table

#  # o.1 solve with for loop
number = (int(input("Enter the number : ")))

for i in range(1, 11):
    print(f"{i} * {number} = {i * number}")


# # no.2 solve this with while loop

N = (int(input("Enter the number : ")))

i = 1
while (i <= 10):
    print(f"{i} * {N} = {i * N}")
    i = i + 1