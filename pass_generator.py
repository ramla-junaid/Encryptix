from tkinter import *
from tkinter import messagebox
import random

def clear_default(event):
    # Function to clear the default text when typing starts
    if passlen.get() == 'Enter Length':
        passlen.set('')
    entry_length.unbind('<FocusIn>')  # Unbind to avoid multiple bindings

def restore_default(event):
    # Restore the default text if the entry is empty
    if not passlen.get():
        passlen.set('Enter Length')
    entry_length.bind('<FocusIn>', clear_default)  # Rebind after restoring

def password_generator():
    try:
        length = int(passlen.get())
        #Do not include space in password
        characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()~' 
        password = ''
        if length >= 8:
            for i in range(length):
                password += random.choice(characters)
            pswd.set(password)
        else:
            # Show a warning message for invalid length
            messagebox.showwarning("Invalid Length", "Please enter a valid password length (minimum 8)")
            pswd.set("")  # Clear the password field
    except ValueError:
        # Show a warning message for invalid number input
        messagebox.showwarning("Invalid Input", "Please enter a valid number for password length")
        pswd.set("")  # Clear the password field

# Create the root window
tk = Tk()
tk.geometry('400x200')  
tk.title('Password Generator')
tk.configure(background='light blue')

# Variables to store password length and generated password
pswd = StringVar()
passlen = StringVar()
passlen.set('Enter Length')  # Default text

# Instructions and input field for password length
Label(tk, text="Enter the number of characters for password\n(Minimum length should be 8)", bg='grey', fg='white').grid(row=0, column=1, columnspan=2, pady=3, padx=10)

entry_length = Entry(tk, textvariable=passlen, width=15)
entry_length.grid(row=1, column=1, pady=15, padx=10)
entry_length.bind("<FocusIn>", clear_default)  # Bind function to clear default text when typing starts
entry_length.bind("<FocusOut>", restore_default)  # Bind function to restore default text when focus is lost

# Button to generate password
Button(tk, text="Generate", command=password_generator, bg='black', fg='white').grid(row=1, column=2, pady=3, padx=10)

# Display to show generated password
Label(tk, text="Generated Password:").grid(row=2, column=1, columnspan=2, pady=3, padx=10)
Entry(tk, textvariable=pswd, state='readonly').grid(row=3, column=1, columnspan=2, pady=3, padx=10, sticky='ew')

# Start the GUI
tk.mainloop()
