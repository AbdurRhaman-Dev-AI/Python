# # now lest write a program using function
# # to convert celsius to fahrenheit

# # celsius = (fahrenheit - 32) * 5/9
# # fahrenheit = (celsius * 9/5) + 32

# # fahrenheit = (celsius * 9/5) + 32
# def convert(Celsius):
#     farenheit = (Celsius * 9 / 5) + 32
#     return farenheit

# Celsius = (int(input("Enter the celsius : ")))
# print(convert(Celsius),"° farenheit")


# # celsius = (fahrenheit - 32) * 5/9

def con(f):
    c = (f - 32) * 9 / 5
    return c

f = (int(input("Enter the farenheit : ")))
print(con(f),"° celsius")