import tkinter as tk
from tkinter import *
from tkinter.ttk import *
import time


window = tk.Tk()


window.title('main')
window.geometry("300x600")

def new_server():
    new_server = tk.Tk("100x100")

    btn4 = Button(new_server, text="make", command=new_server.destroy)
    btn4.pack(side=BOTTOM)

def profile():
    profile = tk.Tk("100x100")

    l2 = Label(profile, text="Pofile:", font=('Times', 20))
    l2.pack(side=TOP)

    e1 = Entry(profile, text='name')
    e1.pack(side=BOTTOM)

def connect():
    connect = tk.Tk("100x100")

    l3 = Label(connect, text="CONNECTING", font=('Times', 20))
    l3.pack(side=TOP)

    progress = Progressbar(connect, orient= HORIZONTAL, length=100, mode='determinate')
    progress.pack(side=BOTTOM)

    def bar():

        progress['value'] = 0
        connect.update_idletasks()
        time.sleep(1)

        progress['value'] = 20
        connect.update_idletasks()
        time.sleep(1)

        progress['value'] = 40
        connect.update_idletasks()
        time.sleep(1)

        progress['value'] = 60
        connect.update_idletasks()
        time.sleep(1)

        progress['value'] = 80
        connect.update_idletasks()
        time.sleep(1)
        progress['value'] = 100

    progress.pack(pady=10) 

    Button(connect, text='confirm', command=bar).pack(pady=10)


l1 = Label(window, text="connect to servers", font=('Times', 20))
l1.grid(row=0, column=0, sticky=W, pady=2)

btn = Button(window, text='connnect', command=connect)
btn.grid(row=1, column=0, sticky=W, pady=2)

btn2 = Button(window, text="new server", command=new_server)
btn2.grid(row=1, column=1, sticky=W, pady=2)

btn3 = Button(window, text="profile", command=profile)
btn3.grid(row=3, column=1, sticky=W, pady=2)



window.mainloop()
