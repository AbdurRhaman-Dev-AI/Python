# # on now lets try the step slicing again

# # first we ave to know what is the step sizing
# # (start , stop , step)
# # (1, 10, 2)

# # for loops

# for i in range(1, 25, 3):
#     print(i)

# # ok now with input valuee

# n = (int(input("Enter the number : ")))
# step = (int(input("Enter a step value : ")))

# for i in range(1, n + 1, step):
#     print(i)

# # now lets do more farthetway
# start = (int(input("Enter the start value : ")))
# stop = (int(input("Enter the stop value : ")))
# step = (int(input("Enter the step value : ")))

# for i in range(start, stop + 1, step):
#     print(i)


# # now lets try all the method with while loop

# i = 0
# while (i, 15, 3):
#     print(i)
#     i = i + 1


# # ok more 

start = (int(input("Enter the start value : ")))
stop = (int(input("Enter the stop value : ")))
step = (int(input("Enter the step value : ")))

i = start
while (i < stop + 1, step):
    print(i)
    i = i + step
    if (i == stop):
        break