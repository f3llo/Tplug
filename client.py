import socket
import threading
import tkinter as tk
import keyboard

root = tk.Tk()

def show_entry_fields():
    print("Username: %s\nPort: %s" % (e1.get(), e2.get()))
    global NAME 
    NAME = e1.get()
    global PORT
    PORT = e2.get()
    PORT = int(PORT)

tk.Label(root, text="Username").grid(row=0)
tk.Label(root, text="Port").grid(row=1)

e1 = tk.Entry(root)
e2 = tk.Entry(root)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

def destroy():
    root.destroy

b1 = tk.Button(root, text='submit', command=lambda:[destroy(), show_entry_fields()])
b1.grid(row=3, column=1, sticky=tk.W,pady=4)
b2 = tk.Button(root, text='Done', command=root.destroy)
b2.grid(row=4, column=0)


root.mainloop()



HEADER = 64
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


def send(name, msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))


connected = True
window = tk.Tk()

label = tk.Label(window, text=f"Connected to: {PORT}")
label.grid(row=2, column=2)

#b1 = tk.Button(window, text="DISCONNECT", command=send("", DISCONNECT_MESSAGE))
#b1.grid(row=0,column=0)

messages = []

e1 = tk.Entry(window)
e1.grid(row=1,column=0)
while connected:
    if keyboard.is_pressed("q"):
        message = e1.get()
        messages.append(message)
        send(NAME, message)
        break

#while connected:
    #send(NAME, NAME)
    #send(f"[CLIENT{NAME}]", input(f"[SELF: {NAME}]"))



window.mainloop()
