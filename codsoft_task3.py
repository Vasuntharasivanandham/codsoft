import tkinter as tk
from tkinter import messagebox
import random
import string

# Function to generate password
def generate_password():
    try:
        length = int(entry_length.get())  # Get the desired length of the password

        # Error if the length is too short
        if length < 4:
            messagebox.showerror("Error", "Password length should be at least 4 characters!")
            return

        # Check which options are selected (letters, numbers, special characters)
        include_upper = var_uppercase.get()
        include_lower = var_lowercase.get()
        include_digits = var_digits.get()
        include_symbols = var_symbols.get()

        if not (include_upper or include_lower or include_digits or include_symbols):
            messagebox.showerror("Error", "Please select at least one option!")
            return

        # Define character sets based on user selection
        char_pool = ""
        if include_upper:
            char_pool += string.ascii_uppercase
        if include_lower:
            char_pool += string.ascii_lowercase
        if include_digits:
            char_pool += string.digits
        if include_symbols:
            char_pool += string.punctuation

        # Generate random password
        password = ''.join(random.choice(char_pool) for _ in range(length))

        # Display generated password
        result_label.config(text="Generated Password: " + password)

    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number for length.")

# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Create and place the input field for password length
label_length = tk.Label(root, text="Password Length:")
label_length.grid(row=0, column=0, padx=10, pady=10)
entry_length = tk.Entry(root)
entry_length.grid(row=0, column=1, padx=10, pady=10)

# Create checkboxes for character set selection
var_uppercase = tk.BooleanVar()
var_lowercase = tk.BooleanVar()
var_digits = tk.BooleanVar()
var_symbols = tk.BooleanVar()

check_uppercase = tk.Checkbutton(root, text="Include Uppercase (A-Z)", variable=var_uppercase)
check_uppercase.grid(row=1, column=0, columnspan=2, padx=10, pady=5)

check_lowercase = tk.Checkbutton(root, text="Include Lowercase (a-z)", variable=var_lowercase)
check_lowercase.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

check_digits = tk.Checkbutton(root, text="Include Digits (0-9)", variable=var_digits)
check_digits.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

check_symbols = tk.Checkbutton(root, text="Include Symbols (!@#$%^&*)", variable=var_symbols)
check_symbols.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

# Create button to generate password
generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.grid(row=5, column=0, columnspan=2, pady=10)

# Create label to display generated password
result_label = tk.Label(root, text="Generated Password:")
result_label.grid(row=6, column=0, columnspan=2, pady=10)

# Start the GUI event loop
root.mainloop()
