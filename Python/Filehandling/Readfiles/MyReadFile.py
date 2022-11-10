


myfile = open("News.txt", "r") # object of file
content = myfile.read() # read all text to one string
content_lines = myfile.readline()

counter = 0

for word in content.split():
    if "years" == word :
        counter +=1

print(content.count("years"))

myfile = open("Cyber.txt", "r") # object of file
content_lines = myfile.readlines()

print(content_lines)
