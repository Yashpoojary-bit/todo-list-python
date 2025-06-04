import tkinter as tk
from tkinter import messagebox

# Colors
BG_COLOR = "#6a0dad"         # Background purple
BTN_COLOR = "#9b59b6"        # Button purple
TEXT_COLOR = "white"
HIGHLIGHT_COLOR = "#dcd6f7"

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("400x500")
        self.root.resizable(False, False)
        self.root.config(bg=BG_COLOR)

        # Title Label
        title = tk.Label(root, text="To-Do List", font=("Helvetica", 20, "bold"), bg=BG_COLOR, fg=TEXT_COLOR)
        title.pack(pady=10)

        # Entry Box
        self.task_entry = tk.Entry(root, font=("Helvetica", 12), width=30)
        self.task_entry.pack(pady=10)

        # Add Task Button
        add_btn = tk.Button(root, text="Add Task", width=20, bg=BTN_COLOR, fg=TEXT_COLOR, command=self.add_task)
        add_btn.pack(pady=5)

        # Task Listbox
        self.task_listbox = tk.Listbox(root, width=35, height=10, font=("Helvetica", 12), selectbackground=HIGHLIGHT_COLOR)
        self.task_listbox.pack(pady=10)

        # Mark Complete Button
        mark_btn = tk.Button(root, text="Mark as Complete", width=20, bg=BTN_COLOR, fg=TEXT_COLOR, command=self.mark_complete)
        mark_btn.pack(pady=5)

        # Remove Task Button
        remove_btn = tk.Button(root, text="Remove Task", width=20, bg=BTN_COLOR, fg=TEXT_COLOR, command=self.remove_task)
        remove_btn.pack(pady=5)

        # Save/Load Buttons
        save_btn = tk.Button(root, text="Save Tasks", width=20, bg=BTN_COLOR, fg=TEXT_COLOR, command=self.save_tasks)
        save_btn.pack(pady=5)

        load_btn = tk.Button(root, text="Load Tasks", width=20, bg=BTN_COLOR, fg=TEXT_COLOR, command=self.load_tasks)
        load_btn.pack(pady=5)

        # Auto-load on start
        self.load_tasks()

    def add_task(self):
        task = self.task_entry.get().strip()
        if task:
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Enter a task!")

    def mark_complete(self):
        try:
            selected = self.task_listbox.curselection()[0]
            task = self.task_listbox.get(selected)
            if not task.startswith("[✓]"):
                self.task_listbox.delete(selected)
                self.task_listbox.insert(selected, "[✓] " + task)
        except IndexError:
            messagebox.showwarning("Warning", "Select a task first!")

    def remove_task(self):
        try:
            selected = self.task_listbox.curselection()[0]
            self.task_listbox.delete(selected)
        except IndexError:
            messagebox.showwarning("Warning", "Select a task to remove!")

    def save_tasks(self):
        tasks = self.task_listbox.get(0, tk.END)
        with open("tasks.txt", "w") as file:
            for task in tasks:
                file.write(task + "\n")
        messagebox.showinfo("Saved", "Tasks saved successfully!")

    def load_tasks(self):
        try:
            with open("tasks.txt", "r") as file:
                tasks = file.readlines()
                self.task_listbox.delete(0, tk.END)
                for task in tasks:
                    self.task_listbox.insert(tk.END, task.strip())
        except FileNotFoundError:
            pass  # No saved tasks yet

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
