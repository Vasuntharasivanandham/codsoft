import tkinter as tk
from tkinter import messagebox, simpledialog

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")

        self.tasks = []

        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=10)

        self.task_label = tk.Label(self.frame, text="Enter a task:")
        self.task_label.pack(side=tk.LEFT)

        self.task_entry = tk.Entry(self.frame, width=30)
        self.task_entry.pack(side=tk.LEFT)

        self.add_task_button = tk.Button(self.frame, text="Add Task", command=self.add_task)
        self.add_task_button.pack(side=tk.LEFT)

        self.tasks_listbox = tk.Listbox(self.root, width=50, height=10)
        self.tasks_listbox.pack(pady=10)

        self.complete_task_button = tk.Button(self.root, text="Mark as Complete", command=self.complete_task)
        self.complete_task_button.pack(pady=5)

        self.delete_task_button = tk.Button(self.root, text="Delete Task", command=self.delete_task)
        self.delete_task_button.pack(pady=5)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.update_tasks_listbox()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def complete_task(self):
        try:
            selected_task_index = self.tasks_listbox.curselection()[0]
            self.tasks[selected_task_index] += " (Completed)"
            self.update_tasks_listbox()
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to mark as complete.")

    def delete_task(self):
        try:
            selected_task_index = self.tasks_listbox.curselection()[0]
            del self.tasks[selected_task_index]
            self.update_tasks_listbox()
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to delete.")

    def update_tasks_listbox(self):
        self.tasks_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.tasks_listbox.insert(tk.END, task)

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
