from multiprocessing import connection
import re
import socket
import sys
from warnings import catch_warnings

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_adders = ('localhost', 5002)
print(server_adders)
sock.bind(server_adders)

sock.listen(1)

while True:
    print('connection from')
    connection, client_adders = sock.accept()
    print(client_adders)
    try:
        while True:
            request = connection.recv(1024)
            print(request)
            if not request:
                break
            else:
                response = 'testing'.encode()
            response = 'testing'.encode()
            connection.send(response)
    finally:
        connection.close()