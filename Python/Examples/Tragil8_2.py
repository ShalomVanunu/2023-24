

def shit_left(my_list):
    new_list = []
    for arg in my_list[1:]:
        new_list.append(arg)
    new_list.append(my_list[0])

#    new_list.append(my_list[1]) # insert second arg
#    new_list.append(my_list[2])
#    new_list.append(my_list[0])
    return new_list


print(shit_left([0,1,"monkey"]))