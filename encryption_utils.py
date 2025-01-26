
'''
FISIERUL PENTRU FUNCTIILE DE CRIPTARE / DECRIPTARE
'''

from cryptography.fernet import Fernet
import os

def generate_key(key_file):
    """Generează și salvează o cheie de criptare."""
    key = Fernet.generate_key()
    with open(key_file, "wb") as file:
        file.write(key)
    return key

def load_key(key_file):
    """Încarcă cheia din fișier sau o generează dacă lipsește."""
    if not os.path.exists(key_file):
        return generate_key(key_file)
    with open(key_file, "rb") as file:
        return file.read()

def encrypt_data(data, key_file):
    """Criptează datele folosind cheia specificată."""
    key = load_key(key_file)
    return Fernet(key).encrypt(data)

def decrypt_data(data, key_file):
    """Decriptează datele folosind cheia specificată."""
    key = load_key(key_file)
    return Fernet(key).decrypt(data)
