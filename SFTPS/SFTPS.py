# SFTPS: Simple Fast TCP Port Scanner
# SFTPS IP START_PORT END_PORT
import socket 
from sys import argv, exit
from threading import Thread 
from resource import getrlimit, RLIMIT_NOFILE, setrlimit


if len(argv) < 4:
	print('Usage: SFTPS IP START_PORT END_PORT')
	exit(0)


soft_limit, hard_limit = getrlimit(RLIMIT_NOFILE)
setrlimit(RLIMIT_NOFILE, (int(argv[3]) - int(argv[2]), hard_limit))



ip_addr = argv[1]

def check(port):
    if socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect_ex((ip_addr, port)) == 0: # 111 connection refused, 0 connected
        print(port)
        
    
        
if __name__ == '__main__':
	for port in range(int(argv[2]), int(argv[3]) + 1):
		Thread(target=check, args=[port]).start()
      