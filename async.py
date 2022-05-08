import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
server_socket.bind(('localhost', 5002))
server_socket.listen()

while True:
    client_socket, addr = server_socket.accept()
    print('connection from', addr)
            
    while True:
        requests = client_socket.recv(1024)

        if not requests:
            getfromserver = print('not can get')
            client_socket.send(getfromserver)
        else:
            response = 'testing'.encode('utf-8')
            client_socket.send(response)

    print('ousite the loop')
    client_socket.close()
