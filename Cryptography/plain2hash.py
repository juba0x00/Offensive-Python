#!/usr/bin/env python3.10
import hashlib
import argparse
from pyperclip import copy

from platform import python_version


def get_hash (text, hashing_algo):
    encoder = bytes(text, 'utf-8')
    hashing_result = ''
    match(hashing_algo.lower()):
        case 'md5': 
            hashing_result = hashlib.md5(encoder).hexdigest()
        case 'sha384': 
            hashing_result = hashlib.sha384(encoder).hexdigest()
        case 'sha3_384': 
            hashing_result = hashlib.sha3_384(encoder).hexdigest()
        case 'sha1':
            hashing_result = hashlib.sha1(encoder).hexdigest()
        case 'sha224':
            hashing_result = hashlib.sha224(encoder).hexdigest()
        case 'sha256':
            hashing_result = hashlib.sha256(encoder).hexdigest()
        case 'sha384':
            hashing_result = hashlib.sha384(encoder).hexdigest()
        case 'sha512':
            hashing_result = hashlib.sha512(encoder).hexdigest()
        case _:   
            return "[!] The script does not support this hash type\n[+] Supported Hashes: \nmd5\nsha1\nsha3_384\nsha3_512\nsha224\nsha384\nsha256\nsha512"

    return hashing_result


if __name__ == '__main__':

    if int(python_version().split('.')[0]) < 3 or int(python_version().split('.')[1]) < 10:
        print('Python 10 required')
        exit(0)

    parser = argparse.ArgumentParser(description='Convert plain text to hash')
    parser.add_argument('text', help='plain text')
    parser.add_argument('hash_algorithm', help='hashing algorithm')
    parser.add_argument('-c', '--clip', action='store_true', help='copy to clipboard')
    args = parser.parse_args()


    hash_result = get_hash(args.text, args.hash_algorithm)

    if (args.clip):
        copy(hash_result)
    else:
        print(hash_result)
