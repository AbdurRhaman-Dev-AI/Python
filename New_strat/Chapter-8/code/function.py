# # write aprogram that will return the avarage of given numbers
# avarage = a + b + c /length of imput list

# # hear def Avg() and inside of this fuction it calls the functionn  definition
def Avg():  # # hear we make a function
    
    a = (int(input("Enter the first number: ")))  # # and hear we indent the input function inside the Avg function
    b = (int(input("Enter the second number: ")))
    c = (int(input("Enter the third number: ")))
    
    average = (a + b + c)/3  # #  and hear we write the average formula to get the averagr of input numbers
    print(average, "%")  # # and hear we print the average

Avg()  # # and hear we call the function but look carefully this call is not inside the indentation of the function
print("Done")  # # and we just print this line extra to show the function section is end
