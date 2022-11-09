import string

abc = string.ascii_lowercase

def  char_freq(letters):
    dict={}
    for letter in letters.lower():
        if letter in abc: # here falls the punction
            dict[letter] = 0 # assign value in key
    for letter in letters.lower():
        if letter in abc:
            dict[letter] += 1

    print(dict)


def main():
    letters ="abbAbcbdbabdbdbabababcbcbaB"
    char_freq(letters)


if __name__ == "__main__" :
    main()

