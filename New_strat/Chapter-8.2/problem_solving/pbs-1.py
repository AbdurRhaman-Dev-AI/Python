# # write aprogram to findout the gratest number of 3 given numbers
# # using function

a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
c = int(input("Enter a number: "))
def gratest(a, b, c):
    if (a > b and a > c):
        return a
    elif (b > a and b > c):
        return b
    elif (c > a and c > b):
        return c
    else:
        return "all are equal"

print(gratest(a, b, c))