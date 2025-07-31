
# def rem(list, word):
#     for item in list:
#         list.remove(word)
#         return list
# list = ["cat", "dog", "mouse",]

# print(rem(list, "dog"))

def rem(list, word):
    n = []
    for item in list:
        if not(item == word):
            n.append(item.strip(word))
    return n

list = ["cat", "dog", "mouse",]

print(rem(list, "dog"))