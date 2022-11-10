

my_file = open("Names.txt", "a") # a - append w - write

for _ in range(5):
    name  = input("The bad guys :")
    my_file.write(name+"\n")