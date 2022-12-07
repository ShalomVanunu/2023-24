file1 = open("targilim.txt", "r")
info = file1.read()
listy = info.split("\n")
tar_list=[]
final_answer = ""
for targil in listy:
    tar_list = targil.split(" ")
    action = tar_list[1]

    if action == '*':
        answer = int(tar_list[0]) * int(tar_list[2])
    elif action == "+":
        answer = int(tar_list[0]) + int(tar_list[2])
    elif action == "/":
        try:
            answer = int(tar_list[0]) / int(tar_list[2])
        except:
            print("error devide 0")
    elif action == "-":
        answer = int(tar_list[0]) - int(tar_list[2])

    final_answer = final_answer + tar_list[0] + action + tar_list[2] + "=" +str(answer) +"\n"

file2 = open("answers.txt", "w")
info2 = file2.write(final_answer)