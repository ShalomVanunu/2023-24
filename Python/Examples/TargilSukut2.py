import random
import string


city_name = input(" enter city name :")
abc = string.ascii_lowercase # abcdef....

def Hagrala(city_name):
    count = 0
    letters = []
    for _ in range(10):
        choose = random.choice(abc)
        if choose in city_name.lower():
            letters.append(choose)
            count +=1
    return count, letters


print(f" Number on times the letters in the city {city_name} :{Hagrala(city_name)}")
