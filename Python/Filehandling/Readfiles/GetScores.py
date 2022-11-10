
my_file = open("Scores.txt", "r")

content = my_file.readlines()
# content_new = my_file.read()
#
# print(content_new.index("Eden"))
# print(content_new[ content_new.index("Eden"):content_new.index("Eden")+4])
print(content[2].split(",")[0])