word = "shallom"
numbers = "0123456789"

for letter in word:
    if "l" ==  letter:
        print(f"l is in {word}")


for letter in range(len(word)):
    if word[letter] ==  "l":
        print(f"l is in {word} in place {letter+1}")
