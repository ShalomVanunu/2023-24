

def add_three_num(a,b,c,d):
    return a+b+c+d

print(add_three_num(10,20,30,40))

### args
def add_numbers(*numbers):
    sum = 0
    for num in numbers:
        sum += num
    return sum

print(add_numbers(20,20,30))


def add_numbers(*name): #"shalom","noa"
    for letter in name:
        print(letter)

add_numbers("shalom","noa")