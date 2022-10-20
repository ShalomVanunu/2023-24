
# Split --> from string to list
text_sen = "my name is shalom vanunu"

split_list = text_sen.split()
senc = ""
for i in split_list[:3]:
    senc += " "+i
print(senc)
print(split_list)
#Join  : --> List to String
new_sting = "\n".join(split_list[:3])
print(new_sting)




