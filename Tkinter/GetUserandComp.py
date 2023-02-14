from tkinter import *
from tkinter import messagebox
import os

window = Tk()
window.title("CyberClass")
window.geometry("300x300")
window.iconbitmap("cyber.ico")
window.resizable(False,False)

label1 = Label(window,text="Cyber Course", font=("David",20))
label1.pack(pady=30)


entry_text = StringVar()
#entry1 = Entry(window,width=20,textvariable=entry_text)
#entry1.pack()
label3 = Label(window,text="", font=("David",10)) # label for show text
label3.pack()


def click():
    comp = os.popen("whoami").read().split("\\")[0]
    user = os.popen("whoami").read().split("\\")[1]
    label3.configure(text=comp+"\n"+user)

def clickclear():
    label3.configure(text="")
    messagebox.showinfo("Complete","Complete")

button1 = Button(window, text="Get User & Compname", command=click, bg="RED")
button1.pack(pady=5)
button2 = Button(window, text="Clear", command=clickclear, bg="GREEN")
button2.pack(pady=5)



window.mainloop()






