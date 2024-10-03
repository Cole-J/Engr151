import socket
import time
from threading import Timer

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 5000))
s.listen(5)

def background_controller():
    message = 'test'
    print('message = f{message}')
    clientsocket.send(bytes(message, "utf-8"))

while True:
    clientsocket, address = s.accept()
    print(f'conection from {address} established')
    background_controller()
