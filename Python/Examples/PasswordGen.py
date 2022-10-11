
## Password Gen

###תו ראשון אות גדולה
## תו אחרון סימן
# באמצע אותיות קטנות ##
## לפחות גדול מ- 4
import string
import random

upper = string.ascii_uppercase
lower = string.ascii_lowercase
punctuation = string.punctuation
password = ""

while True:
    password_len =  int(input("write the length of Password \n"))

    if password_len>=6 :
        password +=random.choice(upper)
        for _ in range(password_len-2):
            password += random.choice(lower)
        password += random.choice(string.punctuation)
        print(password)
    else:
        print("enter password length grater than 6")
        continue




