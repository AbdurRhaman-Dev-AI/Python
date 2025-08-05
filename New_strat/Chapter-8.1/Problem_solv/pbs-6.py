# # write a program by help of functions to convert Inch to cm
# # inch = cm * 2.54
# # cm = inch / 2.54

# # inch to centimeter

# def convert(inch):
#     cm = inch * 2.54
#     return cm

# inch = (int(input("Enter the inch : ")))
# print(convert(inch),"cm")


# # centimeter to inch

def con(cm):
    inch = cm / 2.54
    return inch

cm = (int(input("Enter the cm : ")))
print(con(cm),"inch")