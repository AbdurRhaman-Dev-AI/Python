# # write a program that can print a multiplecation tabile og given number

num = (int(input("Enter a number : ")))

for i in range(1, 11):
    print(f"{num} * {i} = {i * num}")
print("Done")