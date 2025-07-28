# now writing a progam to know the grad of the studen by there exam marks

marks = (int(input("Enter your marks : ")))

if (marks >= 101):
    print("Your marks is invalid")
    print("try again with valid marks", marks)

elif (marks >= 90 and marks <= 100):
    print("Congratulations you got Golden A+ grade")
    print("your marks is ", marks)

elif (marks >= 80 and marks <= 89):
    print("Congratulations you got A+ grade")
    print("your marks is ", marks)

elif (marks >= 60 and marks <= 79):
    print("Congratulations you got A grade")
    print("your marks is ", marks)

elif (marks >= 50 and marks <= 59):
    print("Congratulations you got B grade")
    print("your marks is ", marks)

else:
    print("You are fail")
    print("your marks is ", marks)

print("Thank you for using this program")
print("this is the end of the program")
