import socket
from tkinter import *
import tkinter as tk
import time

HEADER = 64
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = socket.gethostbyname(socket.gethostname())

root = tk.Tk()
root.geometry("250x200")

lb1 = Label(root, text="Port")
lb1.grid(row=0, column=0)
lb2 = Label(root, text="Username")
lb2.grid(row=1, column=0)

e1 = Entry(root)
e1.grid(row=0, column=1)

e2 = Entry(root)
e2.grid(row=1, column=1)


def get_entry():
    global PORT
    PORT = int(e1.get())
    global NAME
    NAME = e2.get()


def connect():
    global client
    ADDR = (SERVER, PORT)
    print(type(ADDR))

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print(client)
    client.connect(ADDR) 


def send(name, msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b'' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)


    print(client.recv(2048).decode(FORMAT))
    received = client.recv(2048).decode(FORMAT)
    text.insert(END, received + "\n")


def send_input(event):
    msg = e3.get()
    e3.delete(0, END)
    send(NAME, msg)

btn1 = Button(root, text="Get data", command=get_entry)
btn2 = Button(root, text="Connect", command=connect)


btn1.grid(row=2, column=1)
btn2.grid(row=3, column=1)


new_window = tk.Toplevel(root)
new_window.title("Chat")
new_window.geometry("200x200")

text = Text(new_window, height=10, width=20)
text.grid(row=0,column=0)

scroll = Scrollbar(new_window)
scroll.grid(row=0, column=1, sticky="ns")
text.config(yscrollcommand=scroll.set)
scroll.config(command=text.yview)


e3 = Entry(new_window)
e3.grid(row=1,column=0, sticky=W)

e3.bind('<Return>', send_input)

root.mainloop()
