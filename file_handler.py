
'''
    FISIERUL PENTRU FUNCTIILE DE SALVARE A LISTEI IN FISIER / INCARCARE A LISTEI DIN FISIER
'''

import os
from encryption_utils import encrypt_data, decrypt_data

FILE_NAME = "todo_list.enc" # Denumirea fisierului unde se vor afla task-urile criptate
KEY_FILE = "key.key" # Denumirea fisierului unde se va afla cheia de criptare

def save_todo_list(tasks):
    separator = '\n'
    tasks_str = separator.join(tasks).encode()
    encrypted_str = encrypt_data(tasks_str, KEY_FILE)

    with open(FILE_NAME, "wb") as file:
        file.write(encrypted_str)


def load_todo_list():
    if not os.path.exists(FILE_NAME):
        return []

    with open(FILE_NAME, "rb") as file:
        encrypted_data = file.read()

    binary_data = decrypt_data(encrypted_data, KEY_FILE)

    separator = '\n'
    return binary_data.decode().split(separator)
