"""Logica de gestiune a to-do list-ului"""

import os  # Modul pentru operații cu fișiere
from cryptography.fernet import Fernet  # Importăm instrumentul de criptare

class ToDoFileManager:


    def __init__(self, file_path="todo_list.txt", key_file="key.key"):
        """
        Inițializează managerul de fișiere. 
        - file_path: Numele fișierului în care salvăm lista de to-do-uri.
        - key_file: Numele fișierului care conține cheia de criptare.
        """
        self.file_path = file_path
        self.key_file = key_file
        self.key = self._load_or_generate_key()

    def _load_or_generate_key(self):
        """
        Încarcă cheia de criptare dintr-un fișier. Dacă nu există, va genera una nouă.
        """
        # Verificăm dacă fișierul cu cheia există deja
        if os.path.exists(self.key_file):
            with open(self.key_file, "rb") as key_file:
                return key_file.read()  # Citim cheia și o returnăm
        else:
            # Dacă nu există, generăm o cheie nouă
            key = Fernet.generate_key()
            with open(self.key_file, "wb") as key_file:
                key_file.write(key)  # Salvăm cheia într-un fișier
            return key

    def save_todo_list(self, tasks):
        """
        Salvează lista de task-uri în fișier, criptată.
        - tasks: O listă de stringuri (task-uri).
        """
        fernet = Fernet(self.key)  # Creăm un obiect de criptare folosind cheia
        with open(self.file_path, "wb") as file:
            # Criptăm lista de task-uri, transformată într-un singur string
            data = "\n".join(tasks).encode()  # Convertim lista într-un șir de caractere
            encrypted_data = fernet.encrypt(data)  # Criptăm șirul de caractere
            file.write(encrypted_data)  # Salvăm în fișier

    def load_todo_list(self):
        """
        Încarcă lista de task-uri din fișier, decriptată.
        Returnează o listă de stringuri (task-uri).
        """
        # Dacă fișierul nu există, returnăm o listă goală
        if not os.path.exists(self.file_path):
            return []

        fernet = Fernet(self.key)
        with open(self.file_path, "rb") as file:
            encrypted_data = file.read()  # Citim datele criptate
            decrypted_data = fernet.decrypt(encrypted_data).decode()  # Decriptăm
            return decrypted_data.split("\n")  # Divizăm șirul în elemente ale listei

    def delete_todo_list(self):
        """
        Șterge fișierul care conține lista de task-uri, dacă există.
        """
        if os.path.exists(self.file_path):
            os.remove(self.file_path)  # Ștergem fișierul
