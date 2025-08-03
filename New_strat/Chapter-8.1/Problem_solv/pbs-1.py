def gratest(a,b,c):
    if (a>b and a>c):
        print(a,"is gratest")
    elif (b>a and b>c):
        print(b,"is gratest")
    elif (c>a and c>b):
        print(c,"is gratest")
    else:
        print("all are equal")

a = 10
b = 20
c = 30
gratest(a,b,c)