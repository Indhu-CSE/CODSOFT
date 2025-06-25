import tkinter as tk
from tkinter import messagebox

# Create the main window
root = tk.Tk()
root.title("To-Do List")
root.geometry("400x450")
root.config(bg="#f0f0f0")

# List to store tasks
tasks = []

# Function to update the listbox
def update_listbox():
    listbox.delete(0, tk.END)
    for task in tasks:
        listbox.insert(tk.END, task)

# Function to add a task
def add_task():
    task = entry.get()
    if task != "":
        tasks.append(task)
        update_listbox()
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

# Function to delete selected task
def delete_task():
    try:
        selected_index = listbox.curselection()[0]
        del tasks[selected_index]
        update_listbox()
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete!")

# Function to mark task as done
def mark_done():
    try:
        selected_index = listbox.curselection()[0]
        tasks[selected_index] = tasks[selected_index] + "*"
        update_listbox()
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to mark as done!")

# GUI Layout
label = tk.Label(root, text="Enter a task:", bg="#f0f0f0", font=("Arial", 12))
label.pack(pady=10)

entry = tk.Entry(root, width=30, font=("Arial", 12))
entry.pack(pady=5)

add_btn = tk.Button(root, text="Add Task", width=15, command=add_task)
add_btn.pack(pady=5)

listbox = tk.Listbox(root, width=40, height=10, font=("Arial", 12), selectbackground="#a0c0f0")
listbox.pack(pady=10)

done_btn = tk.Button(root, text="Mark as Done", width=15, command=mark_done)
done_btn.pack(pady=5)

delete_btn = tk.Button(root, text="Delete Task", width=15, command=delete_task)
delete_btn.pack(pady=5)

exit_btn = tk.Button(root, text="Exit", width=15, command=root.destroy)
exit_btn.pack(pady=20)

# Run the main loop
root.mainloop()
