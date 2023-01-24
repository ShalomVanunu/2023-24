import os

#os.system("notepad")
os.system(r'C:\\Program Files\\Microsoft Office\\Office16\\winword.exe')
# get the user  login
result = os.popen("whoami").read()
print(result.split('\\')[1])


