import os
try:
    os.mkdir("Libi")
except:
    pass

list_dir = os.listdir()
for file in list_dir:
    if file == "BasicOS.py":
        os.rename(file,"BasicOS1.py")
os.chdir("Libi")
file = open("libi.txt",'w')
file.write("Good Day")
file.close()
#os.remove("libi.txt")
print(os.getcwd())
