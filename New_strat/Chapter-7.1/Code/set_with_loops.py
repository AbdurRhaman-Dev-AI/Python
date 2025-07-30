# now write a program that will print items of the set using loops

# ok try with for loops

set = {"Hot", "Cold", "Warm", "Chilly"}
print(type(set))

for i in set:
    print(i)


# ok now write the same program using while loop

# and one of the most importand thing is that is
# first we have to convert set in to list
# to perform this operation in while loop 
# but we don't have to do it in for loop

# ihis is not converting set in to list so we got error
# Set = {
#     "Japan",
#     "Thaiwan",
#     "South korea",
#     "Indonesia"
# }
# print("The type is", type(Set))
# i = 0
# while (i < len(Set)):
#     print(Set[i])
#     i = i + 1

# ok now we convert set in to list

Set = {
    "Japan",
    "Thaiwan",
    "South korea",
    "Indonesia"
}
set = list(Set)   # hear we convert set in to list
print("The type is", type(set))

i = 0
while (i < len(set)):  # hear we use the small set not the Big Set
    print(set[i])
    i = i + 1