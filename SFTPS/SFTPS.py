# SFTPS: Simple Fast TCP Port Scanner
import socket 
from sys import argv 
from cProfile import Profile 
import pstats 
from threading import Thread 
# STPS IP START_PORT END_PORT

if len(argv) < 4:
	print('Usage: STPS IP START_PORT END_PORT')
	quit()


ip_addr = argv[1]

def check(port):

	if socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect_ex((ip_addr, port)) == 0: # 111 connection refused, 0 connected
		print(port)

def main():
	for port in range(int(argv[2]), int(argv[3]) + 1):
		Thread(target=check, args=[port]).start()


if __name__ == '__main__':
    with Profile() as pr:
        main()
    
    stats = pstats.Stats(pr)
    stats.sort_stats(pstats.SortKey.TIME)
    # stats.print_stats()
    stats.dump_stats(filename='profiling_threading.prof')