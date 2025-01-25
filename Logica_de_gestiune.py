import os  # Pentru operațiuni cu fișiere
from cryptography.fernet import Fernet  # Pentru criptare și decriptare

class ToDoFileManager:
    def __init__(self, file_path="todo_list.txt", key_file="key.key"):
        """
        Inițializează managerul de fișiere.
        - file_path: Fișierul în care se salvează lista de to-do.
        - key_file: Fișierul cu cheia de criptare.
        """
        self.file_path = file_path
        self.key_file = key_file
        self.key = self._load_or_generate_key()

    def _load_or_generate_key(self):
        """
        Încarcă cheia de criptare dintr-un fișier. 
        Dacă nu există, generează una nouă și o salvează.
        """
        if os.path.exists(self.key_file):
            with open(self.key_file, "rb") as f:
                return f.read()
        
        # Generăm o cheie nouă
        key = Fernet.generate_key()
        with open(self.key_file, "wb") as f:
            f.write(key)
        return key

    def save_todo_list(self, tasks):
        """
        Salvează lista de task-uri în fișier, criptată.
        - tasks: O listă cu task-uri (string-uri).
        """
        fernet = Fernet(self.key)
        with open(self.file_path, "wb") as f:
            data = "\n".join(tasks).encode()  # Transformăm lista într-un șir de caractere
            f.write(fernet.encrypt(data))  # Criptăm și scriem în fișier

    def load_todo_list(self):
        """
        Încarcă lista de task-uri din fișier și o returnează decriptată.
        """
        if not os.path.exists(self.file_path):
            return []  # Dacă fișierul nu există, returnăm o listă goală

        fernet = Fernet(self.key)
        with open(self.file_path, "rb") as f:
            encrypted_data = f.read()
            return fernet.decrypt(encrypted_data).decode().split("\n")  # Decriptăm și împărțim în listă

    def delete_todo_list(self):
        """
        Șterge fișierul care conține lista de to-do, dacă există.
        """
        if os.path.exists(self.file_path):
            os.remove(self.file_path)
