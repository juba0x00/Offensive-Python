from chat import Chat
from sys import argv

try:
    chat = Chat(is_server=False)
    chat.connect_to(argv[1], int(argv[2]))
    while True:
        chat.send_message()
        chat.recv_message()

except KeyboardInterrupt:
    print('Exiting...')

except BrokenPipeError:
    print('connection lost...')
