# #functions 

# A = 9
# B = 8
# gmean = (A * B) /( A + B)
# C = 8
# D = 7

# gmean1 = (C * D) / (C + D)
# print(gmean)
# print(gmean1)


# A = int (input("Enter the number A = "))
# B = int (input("Enter the number B = "))

# gen = (A * B)/(A + B)
# print(gen)




# def calculate (A ,B):
#     gen = (A * B)/(A + B)
#     print(gen)
# A = 9
# B = 10
# if(A > B):
#     print("A is greater = ", A)
# elif(A == B):
#     print("A",A," and B",B,"Both are equal  ")
# else:
#     print("B is greater = " , B)
# calculate(A, B)



# def calculate (A ,B):
#     gen = (A * B)/(A + B)
#     print(gen)
    
# A = int (input ("Enter the number A = "))
# B = int (input ("Enter the number B = "))

# if(A > B):
#     print("A is greater = ", A)
# elif(A == B):
#     print("A",A," and B",B,"Both are equal  ")
# else:
#     print("B is greater = " , B)
# calculate(A, B)



def calculate (A , B):
    mean = (A * B)/(A + B)
    print(mean)
    
def isgreater (A , B):
    if(A > B):
        print("A is greater = ", A)
    elif(A == B):
        print("A",A," and B",B,"Both are equal  ")
    else:
        print("B is greater = " , B)
        
def isless (A , B):
    pass

    
A = 91
B = 10

isgreater(A, B)
calculate(A, B)

C = 120
D = 15

isgreater(C, D)
calculate(C, D)