

while True :
    try :
        a = int(input("Enter No.1"))
        b = int(input("Enter No.2"))
        print("a/b = ",a//b)
        file = open("names1.txt", "r")
        content_file = file.read()
        print(content_file)
    except ZeroDivisionError :
        print("ZeroDivisionError")
    except FileNotFoundError :
        print("FileNotFoundError")
    except:
        print("Other Error")
    #except ValueError:
    #    print("ValueError")
