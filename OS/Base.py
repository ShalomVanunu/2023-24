import os

#cwd = os.getcwd()
list_of_files = os.listdir() # get the list of files in OS library
print(list_of_files)
try:
    os.mkdir("shalom")
except:
    pass
os.chdir("shalom")
file = open("shalom.txt","w")
file.write("Shalom Shalom")
file.close()

