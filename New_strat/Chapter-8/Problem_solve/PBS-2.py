# # write a program that will convert the the Ceilsius to fahrenheit using function

# # now the formula to convert the celcius to fahrenheit is
# # c/5 = (f-32)/9
# # 5 * (f-32)/9

# # now but first try this formula

# f = (int(input("Enter the farenheit temperature : ")))
# c = 5*(f - 32)/9
# print("the celcius temperature is ", c)


# ok now lets try this using function

# def temperature():
#     f= (int(input("Entert the farenheit temperature : ")))
#     c = (5 * (f - 32)/9)
#     print("the celcius temperature is ", c)

# temperature()


# # ok now try the same program but in diftent approch

def temperature():
    return (5 * (f - 32) / 9)
f = (int(input("Enter the farenheit temperature : ")))
c = temperature()
print(c)