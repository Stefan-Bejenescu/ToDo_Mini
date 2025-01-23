import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from file_handler import save_todo_list, load_todo_list


class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List with Due Dates")
        
        # Defineste aici componentele de GUI
        
        # Vom avea nevoie de un grid, ale carui entry-uri vor fi task-urile din lista
        # Fiecare entry va avea un camp text, care reprezinta task-ul, si un alt camp text, care va reprezenta
        # termenul limita, in format YYYY-MM-DD
        # Informatiile din grid vor fi incarcate folosind functia load_todo_list - aceasta returneaza un vector
        # cu denumirile si due dates-urile task-urilor
        
        # In plus, mai avem nevoie de un input unde sa scriem numele task-ului, unul unde sa scriem due date-ul,
        # un buton de Adauga task si unul de Sterge task
        
        # Butonul de Adauga task trebuie sa afiseze o eroare daca vreunul sau ambele din campurile text sunt
        # goale atunci cand se da click. Command-ul lui va fi self.add_task, adica metoda definita mai jos.
        
        # Butonul de Sterge task trebuie sa stearga un element doar daca s-a dat click pe element mai intai, si
        # sa afiseze o eroare daca s-a dat click pe el fara sa se fi selectat inainte unul din task-urile din
        # lista. Command-ul lui va fi self.delete_task, adica metoda definita mai jos.
        pass

    def add_task(self):
        # Butonul actioneaza asupra text-ului introdus in fiecare din cele doua campuri (daca exista)
        task = self.entry.get().strip()
        due_date = self.date_entry.get().strip()

        # Daca nu exista text in task, afiseaza un warning si opreste functia

        # Valideaza formatul text-ului due_date (daca este oferit un due_date, acest camp poate fi gol pentru
        # task-uri fara un due date)

        # Creeaza un string cu Task-ul si Due Date-ul, asa cum va fi afisat in lista din aplicatie
        # Adauga string-ul in lista
        # Sterge textul din cele doua campuri de input

        # Salveaza lista folosind self.save_todo_list()

    def delete_task(self):
        # Obtine index-ul selectat din lista folosind self.<numele_listei>.curselection()[0] (cred)
        # Sterge index-ul obtinut din lista
        # Salveaza lista folosind self.save_todo_list()
        pass

    def save_todo_list(self):
        # Obtine toate string-urile sub forma de vector din lista intr-o variabila tasks
        # Apeleaza save_todo_list(tasks)
        pass

    def load_todo_list(self):
        # Obtine lista de task-uri sub forma de vector, folosind load_todo_list(), intr-o variabila tasks
        # Itereaza prin tasks folosind un for si insereaza in lista din GUI fiecare element al acestuia
        pass


if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
