# # Write aprogram that will define and print the prime numbers

# # with for loop

# number = (int(input("Enter a number : ")))

# for i in range(2, number):
#     if number % i == 0:
#         print("It is not a prime number")
#         break
# else:
#     print("It is a prime number")

# # now with while loop

number = (int(input("Enter a number : ")))

i = 2
while (i < number):
    if number % i == 0:
        print("It's not a prime number")
        break
    i = i + 1
else:
    print("It is a prime number")