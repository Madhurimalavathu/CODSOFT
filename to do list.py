import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Hey you enter a specific task!!")

def delete_task():
    try:
        selected_task_index = listbox.curselection()[0]
        listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Hey you must select a specific task to delete!!")

# Create the main window
root = tk.Tk()
root.title("My Reminder to do list :)")

# Create and configure a listbox to display tasks
listbox = tk.Listbox(root, selectmode=tk.SINGLE)
listbox.pack(pady=10)

# Create an entry widget for adding new tasks
entry = tk.Entry(root)
entry.pack(pady=10)

# Create buttons for adding and deleting tasks
add_button = tk.Button(root, text="Add me :)", command=add_task)
delete_button = tk.Button(root, text="Delete me :(", command=delete_task)
add_button.pack()
delete_button.pack()

# Start the main GUI event loop
root.mainloop()
