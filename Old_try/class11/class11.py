# X = 4

# match X:
    
#     case 0:
#         print("X is zero")

#     case 4 if X % 2 == 0:
#         print("X is even")

#     case _ if X < 10:
#         print("X is less than 10")


Day = int (input("Enter a day = "))

match Day:
    case 1:
        print("Saturday")
    case 2:
        print("sunday")
    case 3:
        print("monday")
    case 4:
        print("tuesday")
    case 5:
        print("wednesday")
    case 6:
        print("thursday")
    case 7:
        print("friday") 