# write a program to print the imtem inside of list using for loop

list = ["Mango", "Apple", "Orange", "Banana", "Grapes"]
# if we do this way it will work but every time we wont know the number of items in the list
# so we do use len() function

# i = 0
# while (i < 5):
#     print(list[i])
#     i = i + 1

# so this way we will know twhat is the exect number of item in list

i = 0
while (i < len(list)):
    print(list[i])
    i = i + 1