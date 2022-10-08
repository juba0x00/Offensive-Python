from requests import get
result = ''
next_port = 1337

current_number = float(0)
IP = "10.10.250.0"

while True: # next_port != 9765 or result != 'STOP'
    try:
        result = get(f'http://{IP}:{str(next_port)}').text
        
        if result == "STOP":
            break
        
        print(result)
        # add 900 23456
        args = result.split()
        operation = args[0]
        new_number = float(args[1])
        next_port = args[2]
        
        if next_port == 9765:
            break
        
        if operation == "add":
            current_number += float(new_number)
        elif operation == "minus":
            current_number -= float(new_number)
        elif operation == "multiply":
            current_number *= float(new_number)
        elif operation == "divide":
            current_number /= float(new_number)
        else: 
            continue
    except Exception as error:
        pass



print(current_number)