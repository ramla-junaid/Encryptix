import tkinter as tk

# Function to evaluate expressions
def evaluate_expression():
    try:
        # Get the expression from the entry widget
        expression = entry.get()
        # Evaluate the expression
        result = str(eval(expression))
        # Update the entry widget with the result
        entry.delete(0, tk.END)
        entry.insert(0, result)
        # Set a flag to indicate that the result is displayed
        global result_displayed
        result_displayed = True
    except Exception as e:
        # Display error message
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Function to update the entry widget
def button_click(value):
    global result_displayed
    if result_displayed:
        # If a result is displayed, clear the entry widget
        entry.delete(0, tk.END)
        result_displayed = False
    current_text = entry.get()
    if value == "C":
        entry.delete(0, tk.END)
    elif value == "=":
        evaluate_expression()
    else:
        new_text = current_text + value
        entry.delete(0, tk.END)
        entry.insert(0, new_text)

# Function to handle keyboard input
def handle_key(event):
    global result_displayed
    if result_displayed:
        # If a result is displayed, clear the entry widget
        entry.delete(0, tk.END)
        result_displayed = False
    key = event.char
    if key in '0123456789':
        button_click(key)
    elif key in '+-*/':
        button_click(key)
    elif key == '\r':  # Enter key
        button_click('=')
    elif key == '\x08':  # Backspace key
        current_text = entry.get()
        entry.delete(0, tk.END)
        entry.insert(0, current_text[:-1])
    elif key.lower() == 'c':
        button_click('C')

# Function to clear entry on click
def clear_entry_on_focus(event):
    entry.delete(0, tk.END)

# Create main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("250x300")  # Set the window size
root.configure(bg="#b6a3b5")  # Light gray background

# Entry widget for showing the expression and result
entry = tk.Entry(root, font=('Serif', 20), borderwidth=2, bg="#ffffff", fg="#000000")
entry.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

# Bind focus event to clear the entry widget
entry.bind('<FocusIn>', clear_entry_on_focus)

# Button layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('C', 4, 2), ('+', 4, 3),
    ('=', 5, 0, 4)
]

# Button styles
button_bg = "#8e718d"  
button_fg = "white"  
button_font = ('Serif', 14)

# Create and place buttons
for button in buttons:
    text = button[0]
    row = button[1]
    column = button[2]
    colspan = button[3] if len(button) > 3 else 1
    tk.Button(root, text=text, width=4, height=1, bg=button_bg, fg=button_fg, font=button_font,
              command=lambda t=text: button_click(t)).grid(row=row, column=column, columnspan=colspan, padx=2, pady=2, sticky="nsew")

# Bind keyboard events to the main window
root.bind('<KeyPress>', handle_key)
root.bind('<BackSpace>', lambda e: handle_key(e))

# Adjust the grid configuration to make buttons stretch properly
for i in range(6):
    root.grid_rowconfigure(i, weight=1)
for i in range(4):
    root.grid_columnconfigure(i, weight=1)

# Flag to indicate whether a result is displayed
result_displayed = False

# Start the GUI event loop
root.mainloop()
