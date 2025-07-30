# hear we are writing a program to print the multiplication table of given numbers

# n = int(input("Enter a number : "))

# for i in range(i == 10): # in this senariyo we try to print the multiplication table
#     print(n * i) # but it will print the multiplication table of 0

# for i in range(11):  # and if we just do this it will start from 0 but we dont want 0 on the multiplication table
#     print(n * i)


# for i in range(1, 11):
#     print(n * i)


# for i in range(1, 11):
#     print(f"{n} * {i} = {n * i}")  # in hear f statment means format
# # so this code mean (format "{n is input} * {i is loop value that hold loop range} = {n * i is input * loop value}")
# # so print(f"{n} * {i} = {n * i}")is the way we format the multiplication table of given number

# clean code

n = (int(input("Enter a number : ")))

for i in range(1, 11):
    print(f"{n} * {i} = {n * i}")