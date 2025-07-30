#  Now we are going to write a multiplication table using while loop

n = (int(input("Enter a number : ")))

i = 1

while i <= 10:
    print(f"{n} * {i} = {n * i}")
    i = i + 1  # we did every thing same like for loop but we have to do i = 1 + 1 or it will start a infinite loop