

def getting_number_only():
    while True:
        num = input("enter number :")
        if num.isdigit():
            return int(num)
        print("Please enter a digits !!")



print("#"*getting_number_only())
print("%"*getting_number_only())
