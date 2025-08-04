# # write a program using function that will convert celsius to farenheit

# # using function

# # the fprmula is f = (c * 9/5) + 32 
# # or c = 5 * (f - 32) / 9

# # ok now try with c = 5 * (f - 32) / 9 formula
# def convert(f):
#     return 5 * (f - 32) / 9
# f = (int(input("Enter the farenheit number: ")))
# print(convert(f), "°C")


# # ok now try with f = (c * 9/5) + 32 formula

def convert(c):
    return (c * 9/5) + 32
c = (int(input("Enter the celsius number: ")))
print(convert(c), "°F")