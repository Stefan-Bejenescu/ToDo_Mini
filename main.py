
'''
    FISIERUL PRINCIPAL, CE CONTINE GUI-UL APLICATIEI
'''

import tkinter as tk
from tkinter import messagebox


class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List with Due Dates")

        # Frame pentru inputuri
        input_frame = tk.Frame(self.root)
        input_frame.pack(pady=10)

        tk.Label(input_frame, text="Task:").grid(row=0, column=0, padx=5)
        self.entry = tk.Entry(input_frame, width=30)
        self.entry.grid(row=0, column=1, padx=5)

        tk.Label(input_frame, text="Due Date (YYYY-MM-DD):").grid(row=1, column=0, padx=5)
        self.date_entry = tk.Entry(input_frame, width=30)
        self.date_entry.grid(row=1, column=1, padx=5)

        # Butoane pentru adăugare și ștergere
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=10)

        add_button = tk.Button(button_frame, text="Adaugă Task", command=self.add_task)
        add_button.grid(row=0, column=0, padx=10)

        delete_button = tk.Button(button_frame, text="Șterge Task", command=self.delete_task)
        delete_button.grid(row=0, column=1, padx=10)

        # Listbox pentru afișarea task-urilor
        self.task_listbox = tk.Listbox(self.root, width=60, height=15)
        self.task_listbox.pack(pady=10)

        # Variabilă pentru stocarea task-urilor în memorie
        self.tasks = []

    def add_task(self):
        task = self.entry.get().strip()
        due_date = self.date_entry.get().strip()

        if not task:
            messagebox.showwarning("Eroare", "Câmpul pentru task nu poate fi gol!")
            return

        if due_date:
            # Validăm formatul due_date
            import re
            if not re.match(r"\d{4}-\d{2}-\d{2}", due_date):
                messagebox.showwarning("Eroare", "Formatul datei trebuie să fie YYYY-MM-DD!")
                return
            display_text = f"{task} (Due: {due_date})"
        else:
            display_text = task

        self.tasks.append(display_text)
        self.task_listbox.insert(tk.END, display_text)
        self.entry.delete(0, tk.END)
        self.date_entry.delete(0, tk.END)

    def delete_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            self.task_listbox.delete(selected_index)
            del self.tasks[selected_index]
        except IndexError:
            messagebox.showwarning("Eroare", "Trebuie să selectați un task înainte de a șterge!")


if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
