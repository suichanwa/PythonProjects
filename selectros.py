import socket
import selectors

selector = selectors.DefaultSelector()
monitoring = []

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
server_socket.bind(('localhost', 5002))
server_socket.listen()

def accept_conecction(server_socket):    
        client_socket, addr = server_socket.accept()
        print('connection from', addr)

        monitoring.append(client_socket)

def send_message(client_socket):

    while True:
        requests = client_socket.recv(1024)

        if requests:
            response = 'testing'.encode()
            client_socket.send(response)
        else:
            client_socket.close()

def loop():
    while True:
        pass



    
if __name__ == '__main__':
    monitoring.append(server_socket)
    accept_conecction(server_socket)
    loop()
