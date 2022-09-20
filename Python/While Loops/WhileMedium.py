
while True :
    name = input("Whats your name :")
    if name.lower() == "itay":
        print("Greate Man")
        break
    elif name.lower() == "shalom":
        continue
    elif len(name) >10:
        print("your name is TooLong")
    print("try again")
