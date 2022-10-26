
def main():
    my_list = ["a","b","c","d","e","f"]
    new_list = (my_list[::2]) #start , stop, step
    print(", ".join(new_list)+", and "+my_list[-1])

if __name__ == "__main__":
    main()
