#________List in python________
#_____And list are mutable  we can change thare content 
# my_list = [1, 2, 3, 4, 5]

# print("This is the main list:", my_list)
# print(my_list[0])
# print(my_list[2:4])

# my_list.append()
# print("This is the updated list:", my_list)

# my_list.append(9)
# print("This is the updated list:", my_list)

# my_list.remove(3)
# print("This is the updated list after removing 3:", my_list)

# my_list.remove((1), (3), (5))# this way it will not work
# print("This is the updated list after removing 1, 3, and 5:", my_list)
#
#_____This is the correct way to remove multiple items from a list 
# my_list.remove(1)
# my_list.remove(3)
# my_list.remove(5)
# print("This is the updated list after removing 1, 3, and 5:", my_list)
# #_______And this way we add multiple item in the list and creat a new list
# my_list.append(7)
# my_list.append(9)
# my_list.append(11)
# print("and now we add in loist and creat a new list", my_list)

friends = ["Apple", "Orange", 5, 345.06, False, "Marin", "Rphan"]

# print(friends)
# print("In hear we print the item no:0 from the list calld friends",friends[0])
# friends[0] = "Mohit"
# print("In this line we chane the friend list item 0 apple to =",friends[0])
# friends.remove(345.06)
# print("upgraded list = ",friends)

# friends[5] = "Mikasa"
# print(friends) # in this list we change marin to mikasa

# And now we will do multiple item change in list
# But it's kinda funny i chose anime characters name to change on my list
friends[0] = "Eren yeager (Attack Titan)"
friends[1] = "Mikasa Ackerman"
friends[4] = "Levi Ackerman (Captain Levi)"
friends[5] = "Armin Arlert (colossal Titan)"
friends[6] = "Zeke Yeager (Beast Titan)"
# print(friends)
friends.remove("Levi Ackerman (Captain Levi)")#if we have to remove item from the liss we have to use it full name if we use number it will not work
friends.remove("Zeke Yeager (Beast Titan)")
friends.remove("Mikasa Ackerman")
friends.remove("Eren yeager (Attack Titan)")
friends.remove("Armin Arlert (colossal Titan)")
print(friends)

friends.append("Cat")
friends.append("Dog")
friends.append("Ant")
print(friends)
