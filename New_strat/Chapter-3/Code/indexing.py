# # lenth of the list

# name = "Marin"

# # ok = len(name)
# # print(ok)  # Output: 5

# # X = name[0]
# # Y = name[1]
# # Z = name[2]
# # v = name[3]
# # w = name[4]
# # print(X)  # Output: M
# # print(Y)  # Output: a
# # print(Z)  # Output: r
# # print(v)  # Output: i
# # print(w)  # Output: n

# print(name[-4:-1])
# print(name[-5:1])



word = "harry"

# X = word[4]
# print(X)  
# X = word[3]
# print(X)  
# X = word[2]
# print(X)  
# X = word[1]
# print(X)  
# X = word[0]
# print(X)  
# X = word[0: 1]
# print(X)  

# And now using negative indexing
# x = word[-1]
# print(x)
# x = word[-2]
# print(x)
# x = word[-3]
# print(x)
# x = word[-4 : -1]
# print(x)
# x = word[-5]
# print(x)

# and now we try random indexing

# a = word[0:1]
# print(a)
# a = word[0:2]
# print(a)
# a = word[0:3]
# print(a)
# a = word[0:4]
# print(a)
# a = word[1:5]
# print(a)


a = word[:] # it means [0:the lenth of string value] so just start from 0 to the end 
print(a)