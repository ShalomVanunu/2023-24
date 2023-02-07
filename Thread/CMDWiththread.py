import os
import threading
import time

def get_coomand():
    cmd_list = []
    for _ in range(5):
        cmd_list.append(input("Write the Command :"))
    return cmd_list

def run_cmd(command):
    result = os.popen(command).read()
    print(result)
    with open("cmd.txt", "a") as file:
        file.write(result)

def main():
    #cmd_list = get_coomand()
    cmd_list = ["whoami","ipconfig","tasklist","systeminfo","ping www.ynet.co.il"]
    start_time = time.perf_counter()
    for command in cmd_list:
        th = threading.Thread(target=run_cmd, args=(command,))
        th.start()
    th.join()
    stop_time = time.perf_counter()
    print("Total time is :", stop_time-start_time)

if __name__ == '__main__':
    main()