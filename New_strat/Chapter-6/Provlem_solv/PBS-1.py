#  write a program to findout wich number is the gratest
# and find out if all numbers are equal

a = int(input("Enter number 1 : "))
b = int(input("Enter number 2 : "))
c = int(input("Enter number 3 : "))
d = int(input("Enter number 4 : "))

if (a > b and a > c and a > d):
    print("Gratest number is : ", a)

elif (b > a and b > c and b > d):
    print("Gratest number is : ", b)

elif (c > a and c > b and c > d):
    print("Gratest number is : ", c)

elif (d > a and d > b and d > c):
    print("Gratest number is : ", d)

else:
    print("All numbers are equal")
