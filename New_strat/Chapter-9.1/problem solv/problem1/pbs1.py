f = open("problem solv/pbs1.txt","r")
c = f.read()
if ("Twinkle" in c):
    print("yes the word twinkle is present in this file")
else:
    print("no thare is no word twinkle in this file")
f.close()