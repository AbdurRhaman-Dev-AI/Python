s = set()
s.add(20)
s.add("20")
s.add(20.0)  # hear we try to add the same balue multiple time by changing the type of the value
print(s)  # but it will return only one time