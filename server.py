#credit: tech with tim
#add specific sended data to clients
#chat function build

import socket 
import threading
import random
import tkinter as tk
import os
import tqdm
from tkinter import filedialog

HEADER = 64
PORT = random.randint(5050,9999)
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def send(name, msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    server.send(send_length)
    server.send(message)
    print(server.recv(2048).decode(FORMAT))

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False

            #print(f"[{addr}]{msg}")
            print(msg)
            #conn.send("[SERVER] Msg recieved".encode(FORMAT))
            conn.send(f"[CLIENT]{addr}{msg}".encode(FORMAT))

    conn.close()

def start():
    server.listen()
    print(f"[LISTENING] server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread =threading.Thread(target=handle_client,args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")


class App(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        self.start()

    def callback(self):
        self.root.quit()

    def run(self):
        self.root = tk.Tk()
        self.root.geometry("80x120")
        self.root.protocol("WM_DELETE_WINDOW", self.callback)


        def open():
            file_path = filedialog.askopenfilename()
            print(file_path)

        btn = tk.Button(self.root, text="select file", command=open)
        btn.grid(row=1,column=0)

        label = tk.Label(self.root, text=f"Server Adress {PORT}")
        label.grid(row=0,column=0)

        btn1 = tk.Button(self.root, text="share", command=self.root.destroy)
        btn1.grid(row=2,column=0)

        self.root.mainloop()


app = App()

print("[STARTING] server is starting... ")
start()


