
start = int(input(" enter start number"))
stop = int(input(" enter stop number"))


def squard_numbers(start,stop):
    squard_list = []
    for num in range(start, stop+1):
        squard_list.append(num**2)
    return squard_list

print(squard_numbers(start,stop))