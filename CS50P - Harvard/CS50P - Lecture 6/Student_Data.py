# # in this code we are using csv module to read the csv file and add some details to complte the data of the student --- IGNORE ---

with open("Student.csv") as file:
    for line in file:
        row = line.rstrip().split(",")
        print(f"{row[0]} lives in {row[1]}")