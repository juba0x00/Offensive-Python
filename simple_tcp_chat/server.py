from chat import Chat
from sys import argv

try:
    chat = Chat(is_server=True)
    chat.start(argv[1])

    while True:
        chat.recv_message()
        chat.send_message()

except KeyboardInterrupt:
    print('Exiting...')

except BrokenPipeError:
    print('connection lost...')
