# # ok first we will see the break stetment in loops

# # # for loop with break

# for i in range(1, 8):
#     if (i == 5):
#         break
#     print(i)
# print("thi is the for loop with break statement")


# # # now with while loops

# i = 1
# while (i < 8):
#     if (i == 6):
#         break
#     print(i)
#     i = i + 1
# print("this is the while loop with break statement")


# # # now lets use the pass statment in loops

# # # pass with for loop
# for i in range(1, 8):
#     pass
# print("this is the for loop with pass statement")



# # # now pass with while loop

# i = 0
# while (i < 8):
#     pass
# print("this is the while loop with pass statement")



# # now use the continue statement in loops

# # continue statment with for loops

# for i in range(1, 8):
#     if (i == 5):
#         continue
#     print(i)
# print("this is the for loop with continue statement")


# # now continue statment with while loop

# # i = 1
# # while (i < 8):
# #     if (i == 5):
# #         continue
# #     print(i)
# #     i = i + 1
# # print("this is the while loop with continue statement")

# # ok watch this care full this while loop is whild ist go infainite for all the 
# # time if we write this code this way

i = 1
while (i < 8):
    if (i == 5):
        i = i + 1
        continue
    print(i)
    i = i + 1