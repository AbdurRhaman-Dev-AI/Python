place = input("Enter the name of your destination: ")

# if place == "Dhaka":
#     print("You should travel by bus.")
# elif place == "Chittagong":
#     print("You should travel by train.")
# elif place == "Cox's Bazar":
#     print("You should travel by plane.")
# elif place == "Sylhet":
#     print("You should travel by car.")
# else:
#     print("Unknown destination.\n may be you should stay at home.")

match place:
    case "Dhaka":
        print("You should travel by bus.")
    case "Rangpur":
        print("You should travel by train.")
    case "Rajshahi":
        print("You should travel by train.")
    case "Chittagong":
        print("You should travel by train.")
    case "Cox's Bazar":
        print("You should travel by plane.")
    case "Sylhet":
        print("You should travel by car.")
    case "Khulna":
        print("You should travel by boat.")
    case "Barisal":
        print("You should travel by boat.")
    case _:
        print("Unknown destination.\n may be you should stay at home.")


# #  in this code we have some similar transports options for different places

# # so we should make our code compact

match place:
    case "Dhaka" | "Commilla":
        print("You should travel by bus.")
    case "Rangpur" | "Rajshahi" | "Chittagong":
        print("You should travel by train.")
    case "Cox's Bazar":
        print("You should travel by plane.")
    case "Sylhet":
        print("You should travel by car.")
    case "Khulna" | "Barisal":
        print("You should travel by boat.")
    case _:
        print("Unknown destination.\n may be you should stay at home.")