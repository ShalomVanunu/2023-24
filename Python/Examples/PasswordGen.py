
## Password Gen

###תו ראשון אות גדולה
## תו אחרון סימן
# באמצע אותיות קטנות ##
## לפחות גדול מ- 4
import string
import random
upper = "ABCDEFGH"
print(random.choice(upper))

while True:
    password_len =  int(input("write the length of Password\n"))

    if password_len>4 :
        pass
    else:
        print("enter password length grater than 4")
        continue




