import threading
import time
import random
import string

def ret_sign():
    signs = string.punctuation ### !@#$%^%^&*&**(*(*))
    return random.choice(signs)

def create_file(sign, counter):
    file = open(f"sign{counter}.txt","w")
    file.write(sign*10000)
    time.sleep(1)


def main():
    start = time.perf_counter()
    for count in range(1,11):
        sign = ret_sign()
        create_file(sign,count)
    stop = time.perf_counter()
    print(f"total time :{stop-start}")

if __name__ == "__main__" :
    main()