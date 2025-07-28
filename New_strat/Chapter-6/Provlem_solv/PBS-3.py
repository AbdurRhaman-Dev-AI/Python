#  write a program to get students' 3 subject marks as input
#  and combine all the subject and find out total parcentage of the student
# And every subject must be grater then 40

Math = int(input("Enter Math marks : "))
Physics = int(input("Enter Physics marks : "))
Chemistry = int(input("Enter Chemistry marks : "))

# check for total percentage
total_percentage = (100 * (Math + Physics + Chemistry)) / 300

if (total_percentage >= 40 and Math >= 38 and Physics >= 38 and Chemistry >= 38):
    print("You are pass", total_percentage, "%")

else:
    print("You are fail", total_percentage, "%")
    print("please try again next year")

print("this is the end of the program")