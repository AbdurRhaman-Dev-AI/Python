# # in this file we will read data from a csv file and store it in a list of dictionaries
# # we use a dictionary to store student data

students = []

with open("students.csv") as file:
    for line in file:
        name, place = line.rstrip().split(",")
        student = {"name":name, "place":place}
        students.append(student)

for student in students:
    print(f"{student['name']} lives in {student['place']}")