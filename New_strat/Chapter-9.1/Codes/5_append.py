string = "ok now this line will be appended in append.txt file"

f = open("append.txt","a")  # # we open this file in (a)append mode
f.write(string)
f.close()

