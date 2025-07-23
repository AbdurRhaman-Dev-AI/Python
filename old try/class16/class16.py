# def theAvarage (A , B):
#     print("The avarage of A and B is = ", (A + B) / 2)

# theAvarage(28, 4)


# def theAvarage (A = 98 , B = 2):
#     print("The avarage of A and B is = ", (A + B) / 2)

# theAvarage()



# def theAvarage (A = 98 , B = 2):
#     print("The avarage of A and B is = ", (A + B) / 2)

# theAvarage(A= 29 , B= 47)



# def theAvarage (A = 98 , B = 2):
#     print("The avarage of A and B is = ", (A + B) / 2)

# theAvarage(B= 47)


# def theAvarage (A = 98 , B = 2):
#     print("The avarage of A and B is = ", (A + B) / 2)

# theAvarage(A= 47)



# def name (fname , lname , mname):
#     print("Hello," ,fname , lname , mname)

# print("Peter","Quill")



def avarage (*numbers):
    
    print(type(numbers)) #this line shows the type of any variable and classes
    
    sum = 0
    for i in numbers:
        sum = sum + i
    #print("The avarage is = ", sum / len(numbers))
    return sum / len(numbers)
    
# avarage( 5, 6)
( 5, 6)