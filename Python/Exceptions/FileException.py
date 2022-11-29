
def read_file(file_name):
    try:
        file  = open(file_name, "r")
        content_file = file.read()
        print(content_file)
    except:
        print("Error")

file_name = input("Enter File Name :")
read_file(file_name)

    #FileNotFoundError