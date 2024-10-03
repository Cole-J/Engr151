import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("Coles_laptop", 50000))

while True:
    print(s.recv(1024).decode("utf-8"))