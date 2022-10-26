import socket

HOST = '0.0.0.0'
PORT = 50
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(5)
    while True:
        conn, addr = s.accept()
        with conn:
            print('Server :: connected by', addr)
            while True:
                data = conn.recv(1024)
                if not data: break
                conn.sendall(data)
