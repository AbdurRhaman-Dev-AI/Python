# # in this code we are use sorted() function split name and plase top to botom upsite down like A-Z
students = []

with open("student.csv") as file:
    for line in file:
        name, place = line.rstrip().split(",")
        students.append(f"{name} lives in {place}")


for student in sorted(students):
    print(student)
