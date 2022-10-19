friends = ['Yuval','EDEN',"Shaked","Shaked",'Ido',9,9.7] # liust []
print(friends)
friends.pop() # delete the last argument
friends.remove("Shaked") # delete specific arg
print(friends)
friends.clear()
print(friends)

new_friends = []
for name in friends:
    if name != "Shaked":
        new_friends.append(name)

print(new_friends)

