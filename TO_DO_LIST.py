import tkinter as tk
from tkinter import messagebox

# Global variable to keep track of task number
task_number = 1

def add_task():
    global task_number  # Use global keyword to modify global task_number

    def add():
        global task_number  
        input_text = enter_task.get(1.0, "end-1c")# Get the text from Text widget

        if input_text == "":
            messagebox.showwarning(title="Warning!", message="Please enter text")
        else:
            # Format the task with bullet and number
            task_text = f"{task_number}. {input_text}"
            task_list.insert(tk.END, task_text)
            task_number += 1  # Increment task number
            added.destroy()  # Close the window after adding the task

    # Create a new window to input task
    added = tk.Tk()
    added.title("Add Task")
    added.geometry("400x150")
    added.configure(bg="#f4f4f4")

    # Text widget to input task description
    enter_task = tk.Text(added, width=50, height=5, font=("Serif", 12), wrap=tk.WORD, bg="#ffffff", fg="#333333")
    enter_task.pack()

    # Button to add the task
    btn_add = tk.Button(added, text="Add Task", command=add, bg="#43A5BE", fg="white", font=("Serif", 12))
    btn_add.pack(pady=10)

    added.mainloop()

def delete_task():
    # Get the index of the selected item
    selected_item = task_list.curselection()
    
    # Check if any item is selected
    if not selected_item:
        messagebox.showerror("Error", "Kindly select a task to delete.")
        return
    
    # Delete the selected item
    task_list.delete(selected_item)

def complete_task():
    # Get the index of the selected item
    selected_item = task_list.curselection()
    
    # Check if any item is selected
    if not selected_item:
        messagebox.showwarning("Warning!", "Kindly select a task to mark as completed.")
        return

    # Get the task and mark it as completed
    task_index = selected_item[0]
    task = task_list.get(task_index)
    marked_task = task + " ✔"
    
    # Update the task in the listbox
    task_list.delete(task_index)
    task_list.insert(task_index, marked_task)

# Create the main window
window = tk.Tk()
window.title("To Do List")
window.geometry("500x400")
window.configure(bg="#f4f4f4")  # Light grey background

# Create a frame for the listbox and scrollbar
frame_task = tk.Frame(window, bg="#EBB8DD")
frame_task.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Create a Listbox widget for displaying tasks
task_list = tk.Listbox(frame_task, bg="#CAE7D3", fg='#333333', height=15, width=50, font=("Arial", 12), selectmode=tk.MULTIPLE)
task_list.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Create a scrollbar for the Listbox
scrollbar = tk.Scrollbar(frame_task, orient=tk.VERTICAL, command=task_list.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Link scrollbar to the Listbox
task_list.config(yscrollcommand=scrollbar.set)

# Buttons
button_frame = tk.Frame(window, bg="#f4f4f4")
button_frame.pack(pady=10, side=tk.BOTTOM, fill=tk.X)

entry_button = tk.Button(button_frame, text="Add Task", width=12, command=add_task, bg="#43A5BE", fg="white", font=("Serif", 12, "bold"), relief=tk.RAISED, padx=10, pady=5)
entry_button.pack(pady=5, side=tk.LEFT, padx=15)

mark_button = tk.Button(button_frame, text="Complete Task", width=12, command=complete_task, bg="#5bb450", fg="white", font=("Serif", 12, "bold"), relief=tk.RAISED, padx=10, pady=5)
mark_button.pack(pady=5, side=tk.LEFT, padx=10)

delete_button = tk.Button(button_frame, text="Delete Task", width=12, command=delete_task, bg="#BF2C34", fg="white", font=("Serif", 12, "bold"), relief=tk.RAISED, padx=10, pady=5)
delete_button.pack(pady=5, side=tk.LEFT, padx=10)

# Start the Tkinter event loop
window.mainloop()
