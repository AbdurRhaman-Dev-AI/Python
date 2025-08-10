f = open("LineS.txt","r")

line = f.readline()  # # if id bo this multiple time then all the line will print
print(line)

line = f.readline()  # # see i print this second time and the next line is printed
print(line)

f.close
print(type(line))