

# program divide


while True :

    a = int(input("Enter No.1"))
    b = int(input("Enter No.2"))
    print("a/b = ",a//b)

    print("Error")

while True :
    try :
        a = int(input("Enter No.1"))
        b = int(input("Enter No.2"))
        print("a/b = ",a//b)
    except:
        print("Error")

    #ZeroDivisionError