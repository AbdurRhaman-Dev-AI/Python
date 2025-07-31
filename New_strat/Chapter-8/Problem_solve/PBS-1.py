# # write a program to print the gratest number of 3 given number using funtion

def Gratest():
    a = (int(input("Enter the first number: ")))
    b = (int(input("Enter the second number: ")))
    c = (int(input("Enter the third number: ")))
    
    if(a > b and a > c):
        return a
    elif(b > a and b > c):
        return b
    elif(c > a and c > b):
        return c
    else:
        return "All are equal"

print(Gratest())