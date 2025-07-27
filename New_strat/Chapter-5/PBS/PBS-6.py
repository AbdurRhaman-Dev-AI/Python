# write a program to take input 4 name and thare fevorite language and print them

d = {}

name = input("Enter the 1st name: ")
lang = input("Enter the 1st language: ")
d.update({name: lang})

name = input("Enter the 2nd name: ")
lang = input("Enter the 2nd language: ")
d.update({name: lang})

name = input("Enter the 3rd name: ")
lang = input("Enter the 3rd language: ")
d.update({name: lang})

name = input("Enter the 4th name: ")
lang = input("Enter the 4th language: ")
d.update({name: lang})

print(d)