
'''
 FISIERUL PENTRU FUNCTIILE DE SALVARE A LISTEI IN FISIER / INCARCARE A LISTEI DIN FISIER
'''

import os
from encryption_utils import encrypt_data, decrypt_data

KEY_FILE = "key.key"
FILE_NAME = "todo_list.enc"  # Fișier pentru salvarea task-urilor

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
