# # for loop with pass statment

# for i in range(10):
#     pass

# # # while loop with pass statment

# i = 0
# while (i < 10):
#     pass

# # break statment with for loop 

# for i in range(1, 8):
#     print(i)
#     if (i == 5):
#         break


# # now break stet ment with while loop
# i = 1
# while (i < 8):
#     print(i)
#     if (i == 4):
#         break
#     i = i + 1

# now continue statment with for loop

# for i in range(1, 7):
#     if (i == 4):
#         continue
#     print(i)

# now try the continue statment with while loop

i = 1
while (i <= 7):
    if (i == 4):
        i = i + 1
        continue
    print(i)
    i = i + 1