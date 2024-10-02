import tkinter as tk
from tkinter import messagebox

# File to store tasks
FILE_NAME = "tasks.txt"

# Load tasks from the file
def load_tasks():
    try:
        with open(FILE_NAME, "r") as file:
            tasks = file.readlines()
            return [task.strip() for task in tasks]
    except FileNotFoundError:
        return []

# Save tasks to the file
def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")

# Add a new task to the list
def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        tasks.append(task)
        save_tasks(tasks)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "You must enter a task.")

# Remove the selected task from the list
def remove_task():
    selected_task_index = listbox.curselection()
    if selected_task_index:
        task = listbox.get(selected_task_index)
        if messagebox.askyesno("Confirm", f"Do you want to remove the task: '{task}'?"):
            listbox.delete(selected_task_index)
            tasks.remove(task)
            save_tasks(tasks)
    else:
        messagebox.showwarning("Warning", "You must select a task to remove.")

# Clear all tasks from the list
def clear_tasks():
    if messagebox.askyesno("Confirm", "Do you want to clear all tasks?"):
        listbox.delete(0, tk.END)
        tasks.clear()
        save_tasks(tasks)

# Initialize the GUI window
root = tk.Tk()
root.title("To-Do List")

# Entry widget for task input
entry = tk.Entry(root, width=50)
entry.pack(pady=10)

# Buttons for add, remove, and clear tasks
frame = tk.Frame(root)
frame.pack(pady=10)

add_button = tk.Button(frame, text="Add Task", width=12, command=add_task)
add_button.pack(side=tk.LEFT, padx=5)

remove_button = tk.Button(frame, text="Remove Task", width=12, command=remove_task)
remove_button.pack(side=tk.LEFT, padx=5)

clear_button = tk.Button(frame, text="Clear Tasks", width=12, command=clear_tasks)
clear_button.pack(side=tk.LEFT, padx=5)

# Listbox to display tasks
listbox = tk.Listbox(root, width=50, height=15)
listbox.pack(pady=10)

# Load existing tasks into the listbox
tasks = load_tasks()
for task in tasks:
    listbox.insert(tk.END, task)

# Start the GUI event loop
root.mainloop()
