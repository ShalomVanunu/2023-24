import time


def func1(symbol1,symbol2, times):
    print(symbol1*times)
    time.sleep(2)
    print(symbol2*times)

def func2 (symbol3, times):
    print(symbol3 * times)

def main():
    symbol1 = "#"
    symbol2 = "@"
    symbol3 = "%"
    times = 15
    func1(symbol1,symbol2,times)
    func2(symbol3, times)


if __name__ == "__main__":
    main()

