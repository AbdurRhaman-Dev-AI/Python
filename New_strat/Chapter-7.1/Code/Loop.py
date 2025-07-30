# # write a code that will print the given number 
# # multiplication table

# number = (int(input("Enter the number : ")))

# for i in range(1, 11):
#     print(f"{number} * {i} = {i * number}")


# # # now write the same program using the while loop

# n = (int(input("Enter the number : ")))

# i = 1
# while (i < 11):
#     print(f"{n} * {i} = {i * n}")
#     i = i + 1


# # now write a program that show the use case of break statment in loops

# # break stetment with for loop 
# # for this statment we have to use if condition that is if i == 8 then break and exit the loop

# for i in range(1, 8):
#     if (i == 5):
#         break
#     print(i)

# # now try with while loop

# i = 1
# while (i < 8):
#     print(i)
#     i = i + 1
#     if (i == 5):
#         break


# # #And now try the continiue statment

# # #continiue statment with for loops

# for i in range(1, 10):
#     if (i == 4):
#         continue
#     print(i)


# #  now lets try with while loop

i = 1
while (i < 8):
    if (i == 4):
        i = i + 1
        continue
    print(i)
    i = i + 1