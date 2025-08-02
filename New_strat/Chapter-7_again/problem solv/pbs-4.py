# user = (input("Enter your name : ")).lower()

# if user.lower().startswith("k"):
#     print("hello", user, "have a nice day")
# else:
#     print("hello", user, "go home")


# user = (input("Enter your name : ")).upper()

# if user.upper().startswith("K"):
#     print("hello", user, "have a nice day")
# else:
#     print("hello", user, "go home")


# # now try the same but with loops

# # for loop


# # for loop
# user = (input("Enter your name : ")).lower()

# for i in user:
#     if i == "k":
#         print("hello", user, "have a nice day")
#         break
# else:
#     print("hello", user, "go home")


# # while loop

user = (input("Enter your name : ")).upper()

i = user
while (i):
    if i.upper().startswith("K"):
        print("hello", user, "have a nice day")
        break
    else:
        print("hello", user, "go home")
        break