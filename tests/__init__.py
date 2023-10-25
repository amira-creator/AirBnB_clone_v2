#!/usr/bin/python3
"""Tests modules for the AirBnB.
"""
import os
from models.engine.file_storage import FileStorage
from typing import TextIO

def clear_stream(stream: TextIO):
    """make the contents of a given stream clear"""
    if stream.seekable():
        stream.seek(0)
        stream.truncate(0)


def delete_file(file_path: str):
    """ check file existance and remove it if existed"""
    if os.path.isfile(file_path):
        os.unlink(file_path)


def reset_store(store: FileStorage, file_path='file.json'):
    """check the given store and reset the items in it"""
    with open(file_path, mode='w') as file:
        file.write('{}')
        if store is not None:
            store.reload()


def read_text_file(file_name):
    """Take a given file then read its content"""
    lines = []
    if os.path.isfile(file_name):
        with open(file_name, mode='r') as file:
            for line in file.readlines():
                lines.append(line)
    return ''.join(lines)


def write_text_file(file_name, text):
    """Take a given file then write a text to it"""
    with open(file_name, mode='w') as file:
        file.write(text)
