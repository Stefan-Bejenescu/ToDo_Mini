
'''
FISIERUL PENTRU FUNCTIILE DE CRIPTARE / DECRIPTARE
'''

from cryptography.fernet import Fernet
import os


def generate_key(key_file):
    '''
        Genereaza o cheie folosind Fernet, pe care o scrie apoi in format binar in
        fisierul key_file (de unde o vom citi in viitor cand vrem sa decriptam continutul fisierului cu
        task-urile din to-do list), si o si returneaza
    '''
    pass


def load_key(key_file):
    '''
        Daca nu exista fisierul key_file (nu s-a generat deja o cheie), apeleaza generate_key si returneaza
        cheia rezultata. Altfel, inseamna ca exista fisierul cu cheia, deci o citeste in format binar
        din acesta.
    '''
    pass


def encrypt_data(data, key_file):
    '''
        Incarca cheia de criptare intr-o variabila (key, de exemplu) (folosind functia de mai sus)
        Creaza un obiect Fernet cu cheia obtinuta
        Cripteaza data cu metoda encrypt() a obiectului Fernet si returneaza rezultatul
    '''
    pass


def decrypt_data(data, key_file):
    '''
        Incarca cheia de criptare intr-o variabila
        Creeaza un obiect Fernet cu cheia obtinuta
        Decripteaza data cu metoda decrypt() a obiectului Fernet si returneaza rezultatul
    '''
    pass
