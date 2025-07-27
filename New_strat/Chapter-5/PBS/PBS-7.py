#  This program is a test if 2 key is same how it will work
#  i know that it will update the value of the key like 2 key is same but balue is defferent it will pritn the last value we inrter 
#  but if 2 key is different then it will print the value perfectly
d = {}
name = input("Enter the 1st name: ")
lang = input("Enter the 1st language: ")
d.update({name: lang})

name = input("Enter the 2nd name: ")
lang = input("Enter the 2nd language: ")
d.update({name: lang})

print(d)