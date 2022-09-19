#!/usr/bin/env python3.10

import argparse
import logging
from pyperclip import copy
from typed_argparse import TypedArgs


def parse_arguments() -> TypedArgs:
    parser = argparse.ArgumentParser(description="xorCrypt")
    parser.add_argument("text", type=argparse.FileType("r"), help="plain text file ")
    parser.add_argument("key", type=argparse.FileType("r"), help="key file")
    parser.add_argument('-c', '--clip', action="store_true", help='copy the result to clipboard')
    return parser.parse_args()


def xorcrypt(plain_text: str, key: str) -> str:
    result = ""
    if len(plain_text) != len(key):
        logging.error('text and key must be the same length')
    else:
        for i in range(0, len(plain_text)):
            result += chr(ord(plain_text[i]) ^ ord(key[i]))

    return result


if __name__ == '__main__':
    args = parse_arguments()
    res = xorcrypt(str(args.text.read()), str(args.key.read()))
    copy(res) if args.clip else print(res)
