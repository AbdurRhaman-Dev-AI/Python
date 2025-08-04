# # write a program using help of function that will convert Inch to centimetet
# # formula is centimeter = 2.54 * inch

def convert(inch):
    if (inch == 0): return
    return 2.54 * inch
inch = (int(input("Enter the inch number: ")))
print(convert(inch), "cm")