import os

#cwd = os.getcwd()
list_of_files = os.listdir() # get the list of files in OS library
print(list_of_files)
try:
    dir_name = input("enter name of directory to create ")
    os.mkdir(dir_name)
except:
    pass
os.chdir("shalom")

file = open("shalom.txt","w")
file.write("Shalom Shalom")
file.close()

