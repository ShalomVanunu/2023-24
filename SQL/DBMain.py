import DBHandle

def main():
    while True:
        choice = input(""" Press 1 to add User
        Press 2 to Delete User
        Press 3 to Show All Users  [q for Quit]\n""")

        if choice == "1":
            DBHandle.add_user()
        elif choice == "2":
            DBHandle.del_user()
        elif choice == "3":
            DBHandle.show_users()
        elif choice == "q":
            break


if __name__ == '__main__':
    main()

