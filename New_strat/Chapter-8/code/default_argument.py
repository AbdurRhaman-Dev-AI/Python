# # write a program that containt defolt arguments values 
# # if user din't give any value then it will use the defolt value it contains

# # so we did def good(name = "Marin", ending = "Good day"): 
# # we give name aregiment a defolt value of "Marin" and ending aregument a defolt value of "Good day"

def good(name = "Marin", ending = "Good day"):
    print("Hi", name)
    print(ending)

good()
good("Harry", "this is the given value" )