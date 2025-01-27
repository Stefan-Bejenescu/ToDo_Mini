
'''
FISIERUL PENTRU FUNCTIILE DE CRIPTARE / DECRIPTARE
'''

from cryptography.fernet import Fernet
import os

def generate_key(key_file):
    key = Fernet.generate_key()
    with open(key_file, "wb") as file:
        file.write(key)
    return key

def load_key(key_file):
    if not os.path.exists(key_file):
        return generate_key(key_file)

    with open(key_file, "rb") as file:
        key = file.read()
    
    return key

def encrypt_data(data, key_file):
    key = load_key(key_file)
    cipher = Fernet(key)
    return cipher.encrypt(data)


def decrypt_data(data, key_file):
    key = load_key(key_file)
    cipher = Fernet(key)
    return cipher.decrypt(data)
 