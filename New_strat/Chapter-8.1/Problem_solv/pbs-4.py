# # Writing a recorcive function to calculate the sum of first n natural given numbers
# # formula sum = n + sum(n-1) 

def sum(n):
    if (n == 1):
        return 1
    return n + sum(n - 1)

n = (int(input("Enter the value : ")))
print(sum(n))