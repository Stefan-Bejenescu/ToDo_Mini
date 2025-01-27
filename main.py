
'''
    FISIERUL PRINCIPAL, CE CONTINE GUI-UL APLICATIEI
'''

import subprocess
import tkinter as tk
from tkinter import messagebox
from datetime import datetime
from file_handler import save_todo_list, load_todo_list
import requests

FLASK_APP_PATH = "sync_to_calendar.py"
FLASK_PORT = 5000
FLASK_APP_URL = f"http://127.0.0.1:{FLASK_PORT}/sync"

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List with Due Dates")

        # Lista de task-uri, in memorie
        self.tasks = []

        # Frame pentru inputuri
        input_frame = tk.Frame(self.root)
        input_frame.pack(pady=10)

        tk.Label(input_frame, text="Task:").grid(row=0, column=0, padx=5)
        self.entry = tk.Entry(input_frame, width=30)
        self.entry.grid(row=0, column=1, padx=5)

        tk.Label(input_frame, text="Due Date (YYYY-MM-DD):").grid(row=1, column=0, padx=5)
        self.date_entry = tk.Entry(input_frame, width=30)
        self.date_entry.grid(row=1, column=1, padx=5)
        current_date = datetime.today().strftime('%Y-%m-%d')
        self.date_entry.insert(0, current_date)

        # Butoane pentru adăugare și ștergere
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=10)

        tk.Button(button_frame, text="Adaugă Task", command=self.add_task).grid(row=0, column=0, padx=10)
        tk.Button(button_frame, text="Șterge Task", command=self.delete_task).grid(row=0, column=1, padx=10)
        tk.Button(button_frame, text="Sincronizeaza cu Google Calendar", command=self.sync_to_calendar).grid(row=0, column=2, padx=10)

        # Listbox pentru afișarea task-urilor
        self.task_listbox = tk.Listbox(self.root, width=60, height=15)
        self.task_listbox.pack(pady=10)

        # Initializarea din fisier a listei in memorie
        self.load_tasks()

    def add_task(self):
        task = self.entry.get().strip()
        due_date = self.date_entry.get().strip()

        if not task:
            messagebox.showwarning("Eroare", "Câmpul pentru task nu poate fi gol!")
            return

        if due_date:
            try:
                due_date_obj = datetime.strptime(due_date, '%Y-%m-%d').date()
                today = datetime.today().date()
                print(due_date_obj, today)
                if due_date_obj < today:
                    messagebox.showwarning("Eroare", "Data trebuie sa fie astazi sau in viitor!")
                    return
            except ValueError:
                messagebox.showwarning("Eroare", "Formatul datei este invalid")
                return

        display_text = f"{task} (Due: {due_date})" if due_date else task
        self.task_listbox.insert(tk.END, display_text)
        self.entry.delete(0, tk.END)
        self.date_entry.delete(0, tk.END)
        current_date = datetime.today().strftime('%Y-%m-%d')
        self.date_entry.insert(0, current_date)
        self.save_tasks()

    def delete_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            self.task_listbox.delete(selected_index)
            self.save_tasks()
        except IndexError:
            messagebox.showwarning("Eroare", "Trebuie să selectați un task înainte de a șterge!")
    
    def save_tasks(self):
        tasks = self.task_listbox.get(0, tk.END)
        save_todo_list(list(tasks))
    
    def load_tasks(self):
        tasks = load_todo_list()
        for task in tasks:
            self.task_listbox.insert(tk.END, task)
    
    def sync_to_calendar(self):
        tasks=[
            {"name": t.split(" (Due: ")[0], "due_date": t.split(" (Due: ")[1][:-1]}
            for t in self.task_listbox.get(0, tk.END) if "(Due: " in t
        ]

        if not tasks:
            messagebox.showwarning("Eroare", "Nu exista task-uri de sincronizat! Doar task-urile cu Due Date se pot sincroniza!")
            return

        try:
            response = requests.post(FLASK_APP_URL, json={"tasks": tasks})
            if response.status_code == 200:
                messagebox.showinfo("Succes", "Task-urile s-au sincronizat la Google Calendar")
            else:
                error_message = response.json().get("error", "Unknown error")
                messagebox.showerror(
                    "Eroare",
                    f"Nu s-au putut sincroniza task-urile la Google Calendar: {error_message}",
                )
        except requests.exceptions.RequestException as e:
            messagebox.showerror("Eroare", f"Nu s-a putut stabili o conexiune la serverul Flask: {e}")

if __name__ == "__main__":
    try:
        # Pornim server-ul de Flask pe fundal
        flask_process = subprocess.Popen(
            ["python", FLASK_APP_PATH],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
    except FileNotFoundError:
        print(f"Error: {FLASK_APP_PATH} not found.")
        exit(1)
    except Exception as e:
        print(f"Failed to start Flask server: {e}")
        exit(1)

    try:
        root = tk.Tk()
        app = ToDoApp(root)
        root.mainloop()
    finally:
        # Inchidem server-ul de Flask odata cu restul aplicatiei
        flask_process.terminate()
