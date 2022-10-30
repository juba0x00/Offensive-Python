# SFTPS: Simple Fast TCP Port Scanner
# SFTPS IP START_PORT END_PORT
import socket
from sys import argv, exit
from threading import Thread
from resource import getrlimit, RLIMIT_NOFILE, setrlimit

if len(argv) < 2:
    print(f'Usage: {argv[0]} IP')
    exit(0)

# increase file descriptors
soft_limit, hard_limit = getrlimit(RLIMIT_NOFILE)
setrlimit(RLIMIT_NOFILE, (65535, hard_limit))

ip_addr = argv[1]
open_ports = []


def check(crnt_port):
    if socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect_ex((ip_addr, crnt_port)) == 0:
        # 111 connection refused, 0 connected
        # print(f'{crnt_port}')
        open_ports.append(crnt_port)


if __name__ == '__main__':
    for port in range(65535):
        Thread(target=check, args=[port]).start()

    print(*open_ports, sep=',')
