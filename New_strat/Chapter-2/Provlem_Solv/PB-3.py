#_____________Problem Solving in Python_____________

# in this code no matter what the value of a is, it will always be a string
a = input ("Enter a number a : ")
print(type(a))

#So we have to try a aproach to give a right type of input

a = int(input("Enter a number a : "))

try:
    int_value = int(a)
    print("The value of a is an integer:", int_value)
except ValueError:
    print("The value of a is not an integer, it is:", a)

try:
    float_value = float(a)
    print("The value of a is a float:", float_value)
except ValueError:
    print("The value of a is not a float, it is:", a)
    
    if a.lower() == 'true' or a.lower() == 'false':
        print("The value of a is a boolean:", a)

    else:
        print("The value of a is a string:", a)

        # this approch kinda works but it is not the best way to do it