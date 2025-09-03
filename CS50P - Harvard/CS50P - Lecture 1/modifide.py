def main():
    x = int(input("Enter the value of x: "))
    if is_even(x):
        print(x, "is an even number")
    else:
        print(x, "is an odd number")

# def is_even(n):
#     if n % 2 == 0:
#         return True
#     else:
#         return False

# or
def is_even(n):
    return n % 2 == 0

main()