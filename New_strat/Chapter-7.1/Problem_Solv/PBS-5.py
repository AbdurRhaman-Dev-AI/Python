# # write a program that gill give the factorial value of given numbers

# # factorial means 5 ! = 1 * 2 * 3 * 4 * 5 * n
# # it will go all the way to input nmber

# # factorial of input number using the for loop

n = (int(input("Enter the number : ")))

product = 1
for i in range(1, n+1):
    product = product * i
print("The factorial of", n, "is", product)
# # or
# print(f"The factorial of {n} is {product}")