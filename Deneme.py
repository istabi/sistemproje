import socket

soket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

HOST = 'localhost'
PORT = 8080

soket.connect((HOST,PORT))

data = soket.recv(1024)

print (data)

soket.send ("Hoşbulduk!")

soket.close()