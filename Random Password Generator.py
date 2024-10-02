import random
import string
import tkinter as tk
from tkinter import messagebox

# Function to generate a random password
def generate_password():
    length = int(length_entry.get())
    include_uppercase = uppercase_var.get()
    include_numbers = numbers_var.get()
    include_special = special_var.get()

    characters = string.ascii_lowercase
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_numbers:
        characters += string.digits
    if include_special:
        characters += string.punctuation

    if length < 1:
        messagebox.showwarning("Warning", "Password length must be at least 1.")
        return

    password = ''.join(random.choice(characters) for _ in range(length))
    password_var.set(password)

# Function to copy the generated password to the clipboard
def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(password_var.get())
    messagebox.showinfo("Copied", "Password copied to clipboard!")

# Initialize the GUI window
root = tk.Tk()
root.title("Random Password Generator")

# Password length
tk.Label(root, text="Password Length:").pack(pady=10)
length_entry = tk.Entry(root)
length_entry.pack(pady=5)
length_entry.insert(0, "12")  # Default length

# Options for uppercase, numbers, and special characters
uppercase_var = tk.BooleanVar()
numbers_var = tk.BooleanVar()
special_var = tk.BooleanVar()

tk.Checkbutton(root, text="Include Uppercase Letters", variable=uppercase_var).pack()
tk.Checkbutton(root, text="Include Numbers", variable=numbers_var).pack()
tk.Checkbutton(root, text="Include Special Characters", variable=special_var).pack()

# Generate button
generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack(pady=10)

# Display generated password
password_var = tk.StringVar()
password_label = tk.Entry(root, textvariable=password_var, font=("Courier", 16), width=30, justify='center')
password_label.pack(pady=10)

# Copy to clipboard button
copy_button = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.pack(pady=10)

# Start the GUI event loop
root.mainloop()
