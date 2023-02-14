from tkinter import *


window = Tk()
window.title("CyberClass")
window.geometry("300x300")
window.iconbitmap("cyber.ico")
window.resizable(False,False)

label1 = Label(window,text="Cyber Course", font=("David",20))
label1.pack(pady=30)
label2 = Label(window,text="Username", font=("David",10))
label2.pack(pady=10)

entry_text = StringVar()
entry1 = Entry(window,width=20,textvariable=entry_text)
entry1.pack()
label3 = Label(window,text="", font=("David",10)) # label for show text
label3.pack()


def click():
    label3.configure(text=entry_text.get())

button1 = Button(window, text="Enter", command=click)
button1.pack(pady=5)


window.mainloop()






