#  #  at fitst we have to under stand what is factorial

# # # factorial 5 = 5! 

# # """
# # factorial(0) = 1
# # factorial(1) = 1
# # factorial(2) = 2 * 1
# # factorial(3) = 3 * 2 * 1
# # factorial(4) = 4 * 3 * 2 * 1
# # factorial(5) = 5 * 4 * 3 * 2 * 1
# # factorial(n) =  n *...* 6 * 5 * 4 * 3 * 2 * 1
# # """ 

# # # this is the dafination of the factrial

# # now try 

def funk(n):
    if (n == 0 or n == 1):
        return 1
    return n * funk(n-1)

n = (int(input("Enter a  number : ")))
print(funk(n))
