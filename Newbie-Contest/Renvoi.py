from requests import get
from sys import argv
from html2text import html2text


def get_valid_number(cookie):
    response = get('https://www.newbiecontest.org/epreuves/prog/prog1.php', cookies=cookie)
    random_number = response.text.split(': ')[1]
    return random_number

def validate_number(random_number, cookie):
    response = get(f'https://www.newbiecontest.org/epreuves/prog/verifpr1.php?solution={random_number}', cookies=cookie)
    return html2text(response.text)

if __name__ == '__main__':
    if len(argv) != 2:
        print(f'Usage {argv[0]} cookie_value')
        exit(0)
        
    else:
        try:
            cookie = {'SMFCookie89': argv[1]}
            valid_number = get_valid_number(cookie)
            print(validate_number(valid_number, cookie))  
        except ValueError as e:
            print(e)