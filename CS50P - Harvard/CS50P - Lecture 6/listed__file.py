# # in hear i'm gonna make the listt.py file code more efficiently and compact size
# # we did the same sorted() function but in a more compact way to print the names in sorted order

with open("names.txt") as file:
    for line in sorted(file):
        print("hello,", line.rstrip())