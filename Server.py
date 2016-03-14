import socket
soket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
HOST = '10.99.15.255'
PORT = 9000

soket.bind((HOST,PORT))
print ('%s:%d server başlatıldı.' %(HOST,PORT))
print ('Kullanıcı bekleniyor.')
soket.listen(1)
while True:
    baglanti,adres = soket.accept()
    print ('Baglanan biri var',adres)