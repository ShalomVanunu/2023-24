#Dictionary { }
#  { Key : Value ,}

My_Dict = { "name" : "shalom" , "age" : 25 , "Professon" : 'Teacher'}

print(My_Dict["name"])
print(My_Dict["age"])
print(My_Dict.values())
print(list(My_Dict.values()))
print(My_Dict.keys())
print(My_Dict.items())

My_Dict["name"] = "Yuval" # assign Value
print(My_Dict.values())
print(My_Dict["name"])

for value in My_Dict.values():
    print(value)




