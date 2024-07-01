import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('127.0.0.1', 12345))
s.send("Hola soy cliente".encode())
response = s.recv(1024).decode()
print(response)