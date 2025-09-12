# # we use a dictionary to store student data
# student = {}

students = []

with open("students.csv") as file:
    for line in file:
        name, place = line.strip().split(",")
        student = {}
        student["name"] = name
        student["place"] = place
        students.append(student)

for student in students:
    print(f"{student['name']} lives in {student['place']}")