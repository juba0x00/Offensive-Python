from socket import socket, AF_INET, SOCK_STREAM


class Chat(socket):
    def __init__(self, is_server=True):
        self.is_server = is_server


    def start(self, port):
        s = socket(AF_INET, SOCK_STREAM)
        s.bind(('0.0.0.0', int(port)))
        s.listen()
        self.connection, self.addr = s.accept()

    def connect_to(self, ip, port):
        self.client = socket(AF_INET, SOCK_STREAM)
        self.client.connect((ip, port))


    def send_message(self):
        message = input('Server> ' if self.is_server else 'Client> ')
        if self.is_server:
            self.connection.sendall(message.encode())
        else:
            self.client.sendall(message.encode())

        if message == 'bye':
            print('Exit...')
            exit(0)

    def recv_message(self):
        if self.is_server:
            data = self.connection.recv(1024).decode()

        else:
            data = self.client.recv(1024).decode()

        print('client> ' if self.is_server else 'Server> ', end='')
        print(data)
        if data == 'bye':
            print('bye')
            exit(0)

