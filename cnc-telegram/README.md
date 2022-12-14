# Command and Control Telegram Bot
*Disclaimer: For experimental purposes only.*

Simple Python 3 demo of Command and Control (C&C) bot. It implements four possible commands:
* List files in a specified directory
* List all active users
* List all running processes
* Write data to a specified file

Some of the commands are implemented by calling the Linux shell commands. On Windows, some of them may not be available. The bot checks Telegram for new incoming messages every 15 seconds.

## Installation
### Obtaining the API key
First of all, you need to have a Telegram account. Afterward, you need to follow the steps given by the [Telegram BotFather](https://telegram.me/botfather). It is a Telegram interface for the creation of user's bots. Starting with a command `/newbot`, you will be asked for the name of your bot and its username. At the end of the process, the BotFather will give you your API key.

### Running the bot
 Once you have your API key, you need to paste it to the file `authorization.py`. Once it is done, you can install the requirements `pip install -r requirements.txt` and run the bot using command `python3 bot.py`.

In your Telegram application, simply start a conversation with your bot. Once it's started, the message showing possible commands is shown. Using the chat, you can send all of the possible commands. The bot will execute them and send you a message with the result of operations.

## Commands

* Directory listing: `ls [path]`  
* Show active users: `users`  
* Show running processes: `processes`  
* Write to file: `write [path] [data]`  
* Terminate the application: `terminate`  

