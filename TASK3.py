import tkinter as tk
from tkinter import messagebox
from datetime import datetime

class TodoApp:
    def __init__(self, master):
        self.master = master
        self.master.title("To-Do List App")
        self.tasks = []
        self.frame_input = tk.Frame(self.master)
        self.frame_input.pack(pady=10)
        self.frame_tasks = tk.Frame(self.master)
        self.frame_tasks.pack(pady=5)
        self.frame_buttons = tk.Frame(self.master)
        self.frame_buttons.pack(pady=5)
        self.label_task = tk.Label(self.frame_input, text="Enter Task:")
        self.label_task.grid(row=0, column=0, padx=5)
        self.entry_task = tk.Entry(self.frame_input, width=40)
        self.entry_task.grid(row=0, column=1, padx=5)
        self.label_deadline = tk.Label(self.frame_input, text="Set Deadline (optional):")
        self.label_deadline.grid(row=0, column=2, padx=5)
        self.entry_deadline = tk.Entry(self.frame_input, width=20)
        self.entry_deadline.grid(row=0, column=3, padx=5)
        self.button_add_task = tk.Button(self.frame_input, text="Add Task", command=self.add_task)
        self.button_add_task.grid(row=0, column=4, padx=5)
        self.listbox_tasks = tk.Listbox(self.frame_tasks, height=15, width=50)
        self.listbox_tasks.pack(side=tk.LEFT, fill=tk.BOTH)
        self.scrollbar_tasks = tk.Scrollbar(self.frame_tasks)
        self.scrollbar_tasks.pack(side=tk.RIGHT, fill=tk.BOTH)
        self.listbox_tasks.config(yscrollcommand=self.scrollbar_tasks.set)
        self.scrollbar_tasks.config(command=self.listbox_tasks.yview)
        self.button_remove_task = tk.Button(self.frame_buttons, text="Remove Task", command=self.remove_task)
        self.button_remove_task.grid(row=0, column=0, padx=5)
        self.button_count_tasks = tk.Button(self.frame_buttons, text="Count Tasks", command=self.count_tasks)
        self.button_count_tasks.grid(row=0, column=1, padx=5)
        self.button_time_spent = tk.Button(self.frame_buttons, text="Time Spent", command=self.time_spent)
        self.button_time_spent.grid(row=0, column=2, padx=5)
    def add_task(self):
        task = self.entry_task.get().strip()
        deadline = self.entry_deadline.get().strip()
        if task:
            if deadline:
                try:
                    deadline = datetime.strptime(deadline, "%Y-%m-%d %H:%M")
                except ValueError:
                    messagebox.showerror("Error", "Invalid deadline format! Please use YYYY-MM-DD HH:MM")
                    return
            else:
                deadline = None
            self.tasks.append({"task": task, "deadline": deadline})
            self.update_task_list()
            self.entry_task.delete(0, tk.END)
            self.entry_deadline.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Task cannot be empty!")
    def remove_task(self):
        try:
            index = self.listbox_tasks.curselection()[0]
            del self.tasks[index]
            self.update_task_list()
        except IndexError:
            messagebox.showerror("Error", "No task selected!")
    def count_tasks(self):
        num_tasks = len(self.tasks)
        messagebox.showinfo("Task Count", f"Total number of tasks: {num_tasks}")
    def time_spent(self):
        # Dummy function, implement as needed
        messagebox.showinfo("Time Spent", "Functionality to track time spent on tasks will be implemented here!")
    def update_task_list(self):
        self.listbox_tasks.delete(0, tk.END)
        for task in self.tasks:
            task_str = task["task"]
            if task["deadline"]:
                task_str += f" (Deadline: {task['deadline']})"
            self.listbox_tasks.insert(tk.END, task_str)
def main():
    root = tk.Tk()
    todo_app = TodoApp(root)
    root.mainloop()
if __name__ == "__main__":
    main()
