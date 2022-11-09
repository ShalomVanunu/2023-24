# List  [ ]
My_List  = ["shalom", 8,4.5, True]
print(My_List[1:3])
My_List[0] = "Eden"
print(My_List[0])
print(dict(My_List))

# Tuple  ( )
My_Tuple = ("shalom", 8,4.5, True)
print(My_Tuple[1:4])
#My_Tuple[0] = "Eden" #Error


#convert from Tuple to List
#Option #1
Converted_List = []
for item in My_Tuple:
    Converted_List.append(item)

#Option #2
Converted_List = list(My_Tuple)
print(Converted_List)

#convert from  List to Tuple
Converted_Tuple = tuple(Converted_List)
print(Converted_Tuple)


Tuple_one = ("shalom",)
print(type(Tuple_one))

Tuple_Num = (34,76,87,34,56,3,6,3)
List_Tuple = [(3,5),(4,6),(1,5)]
print(sorted(List_Tuple)[1][1])