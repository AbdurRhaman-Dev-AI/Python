#  write a code that will print item of the string using loops

# # lets try with for loops

String = "Hello World"
for i in String:
    print(i)

# # ok now try a difrent aproach 
# # in this code we are printing the string by its length
# # it will print by depending on the length of the string
# # so if lenth is 10 then it will print 10 times

# # hear we are printing the string by its length
S = "Marin"
for i in range(len(S)):
    print(S)

# # now we can print a string how many time we want

S = "Marin"

for i in range(10):
    print(S)


# # Now lets try all of thos method by using while loop

S = "Marin"
i = 0
while (i < len(S)):
    print(S)
    i = i + 1


# # now lets print the item inside of the string

S = "Marin"
i = 0  #  hear we give the loop whare to start
while (i < len(S)):  # hear we give the loop whare to end
    print(S[i])  # and hear we give accass to the itemd of the string
    i = i + 1  # and hear we give the step size to the loop like how many step it will take every time untill the loop end or exit

# And now lets print the string how many time we want

S = "Cat"
i = 0
while (i < 10):
    print(S)
    i = i + 1