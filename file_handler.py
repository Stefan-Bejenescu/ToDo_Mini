
'''
 FISIERUL PENTRU FUNCTIILE DE SALVARE A LISTEI IN FISIER / INCARCARE A LISTEI DIN FISIER
'''

import os
from encryption_utils import encrypt_data, decrypt_data

FILE_NAME = "todo_list.enc"  # Fișier pentru salvarea task-urilor

def save_tasks(tasks):
    if not tasks:
        return  # Nu salvăm nimic dacă lista e goală

    combined_tasks = "||".join(tasks)  # Combinăm task-urile într-un singur string
    encrypted_data = encrypt_data(combined_tasks.encode())  # Criptăm datele

    with open(FILE_NAME, "wb") as file:
        file.write(encrypted_data)  # Scriem datele criptate în fișier

def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []  # Dacă fișierul nu există, returnăm o listă goală

    with open(FILE_NAME, "rb") as file:
        encrypted_data = file.read()  # Citim datele criptate

    decrypted_text = decrypt_data(encrypted_data).decode()  # Decriptăm și convertim în text
    return decrypted_text.split("||")  # Împărțim textul în task-uri
