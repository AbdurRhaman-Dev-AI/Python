# # now we are writing a program using function
# # to find out the gratest number of three given numbers

def num(a, b, c):
    if (a > b and a > c):
        return a
    elif (b > a and b > c):
        return b
    elif (c > a and c > b):
        return c
    else:
        return "all are equal"

a = (int(input("Enter the numbr : ")))
b = (int(input("Enter the numbr : ")))
c = (int(input("Enter the numbr : ")))

print(num(a,b,c))