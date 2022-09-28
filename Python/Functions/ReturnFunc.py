

def calc_average(a,b,c):
    return (a+b+c)/3

def calc_average_sum(a,b,c):
    return (a+b+c)/3, a+b+c

print(calc_average(10,20,30))
average, sum = calc_average_sum(10,20,30)
print(average,sum)
print(calc_average_sum(10,20,30))