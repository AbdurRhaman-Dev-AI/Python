
def remo(list, word):
    n = []
    for item in list:
        if not(item == word):
            n.append(item.strip(word))
    return n
    
list = ["Apple", "Banana", "Cherry"]

print(remo(list, "na"))
