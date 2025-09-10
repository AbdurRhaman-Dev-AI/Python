# # in this code we upgrade our old code student_data.py by using csv file to
# # store the data of students names and their places whare they live

with open("student.csv") as file:
    for line in file:
        name, place = line.rstrip().split(",")
        print(f"{name} lives in {place}")