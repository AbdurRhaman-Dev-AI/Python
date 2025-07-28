# now we are writing a program to detect spam comment and massage

p1 = "make a lot of money"
p2 = "buy now"
p3 = "subscribe this"
p4 = "click this"
p5 = "free gift"

message = input("Enter your message : ")

if ((p1 in message) or (p2 in message) or (p3 in message) or (p4 in message) or (p5 in message)):
    print("this is spam")

else:
    print("this is not spam")

print("this is the end of the program")