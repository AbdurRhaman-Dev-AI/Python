#  write a program to get students' 3 subject marks as input
#  and combine all the subject and find out total parcentage of the student

Math = int(input("Enter Math marks : "))
Physics = int(input("Enter Physics marks : "))
Chemistry = int(input("Enter Chemistry marks : "))

# check for total percentage
total_percentage = (100 * (Math + Physics + Chemistry)) / 300

if (total_percentage >= 40):
    print("You are pass", total_percentage, "%")

else:
    print("You are fail")
    print("Your total persentage is ", total_percentage)
    print("your this year is wasted gone ,haha loser")
    print("ha ha try again next year")
    print("Cradit to steven for this dailogue -_- ")

print("this is the end of the program")