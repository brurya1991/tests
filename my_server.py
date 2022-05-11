import socket
from threading import Thread
from time import sleep


class ServerHttpUtils:

    def __init__(self):
        self.SERVER_HOST = '127.0.0.1'
        self.SERVER_PORT = 8000
        self.server_socket = None

    def create_server(self):
        # Create socket
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind((self.SERVER_HOST, self.SERVER_PORT))
        self.server_socket.listen(1)
        print('Listening on port %s ...' % self.SERVER_PORT)
        self.start_server()

    def close_server(self):
        # Close socket
        print("Shutting down the server...")
        self.server_socket.close()
        sleep(30)

    def connect(self):
        while True:
            # Wait for client connections
            client_connection, client_address = self.server_socket.accept()
            # Get the client request
            request = client_connection.recv(1024).decode()
            print(request)
            # Send HTTP response
            response = 'HTTP/1.0 200 OK'
            client_connection.sendall(response.encode())
            client_connection.close()

    def start_server(self):
        # Set server connection for client as separate Thread
        thread1 = Thread(target=self.connect)
        thread1.start() 
