import socket

HOST = '192.168.208.145'
PORT = 50
q = input("Please enter question:") + '?'
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(q.encode())
    data = s.recv(1024).decode()
print('Clent "" recirved ', repr(data))
