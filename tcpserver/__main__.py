from multiprocessing import connection
import socket
from warnings import catch_warnings

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_adders = ('localhost', 5002)
print(server_adders)
sock.bind(server_adders)

sock.listen(1)

while True:
    print('connection from')
    conn, client_adders = sock.accept()
    print(client_adders)
    while True:
        data = conn.recv(1024)
        if not data:
            break
        print(data)
        conn.send(data)
        if data == b'quit':
            break