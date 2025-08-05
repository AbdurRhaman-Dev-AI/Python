# # write a multiplication table by using function
# # but in reverse order

# # formula we will use (f"{i} * {n} = {n * i})

def table(n):
    for i in range(10, 0, -1):
        print(f"{n} * {i} = {n * i}")

n = (int(input("Enter the value : ")))
table(n)