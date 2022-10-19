


def sum_calc(*numbers): # use *arg  input
    sum=0
    for num in numbers:
        if num % 5 == 0:
            sum +=num
    return sum

sum_calc(12,15,20,16,30,45)