# # ok now print the multiplication table using loop
# # but in reverce order  like value will go 10 to 1


# # for loop

# number = (int(input("Enter a number: ")))

# for i in range(10, 0, -1):  # # in hear insteand (1, 11) we use (10, 0, -1)
#     print(f"{number} * {i} = {number * i}")


# # now with while loop

number = (int(input("Enter a number: ")))

i = 10
while (10 > 1):
    print(f"{i} * {number} = {i * number}")
    i = i - 1  # # hear the magic it will go to nagative every time get 1 value nagative value
    if (i == 0):  # # and yap we just have to break the loop or it will go infinite
        break
