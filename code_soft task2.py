import tkinter as tk
from tkinter import messagebox

def perform_calculation():
    try:
        # Get the values from the entry fields
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operation = operation_var.get()

        # Perform the selected arithmetic operation
        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 == 0:
                messagebox.showerror("Error", "Division by zero is not allowed!")
                return
            result = num1 / num2
        else:
            result = "Invalid Operation"

        # Display the result in the result label
        result_label.config(text="Result: " + str(result))

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers")

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Create and place the number input fields
label_num1 = tk.Label(root, text="Enter first number:")
label_num1.grid(row=0, column=0, padx=10, pady=10)
entry_num1 = tk.Entry(root)
entry_num1.grid(row=0, column=1, padx=10, pady=10)

label_num2 = tk.Label(root, text="Enter second number:")
label_num2.grid(row=1, column=0, padx=10, pady=10)
entry_num2 = tk.Entry(root)
entry_num2.grid(row=1, column=1, padx=10, pady=10)

# Create and place the operation options
operation_var = tk.StringVar()
operation_var.set("+")  # Default value

label_operation = tk.Label(root, text="Choose an operation:")
label_operation.grid(row=2, column=0, padx=10, pady=10)

operation_menu = tk.OptionMenu(root, operation_var, "+", "-", "*", "/")
operation_menu.grid(row=2, column=1, padx=10, pady=10)

# Create the calculate button
calculate_button = tk.Button(root, text="Calculate", command=perform_calculation)
calculate_button.grid(row=3, column=0, columnspan=2, pady=10)

# Create the result label
result_label = tk.Label(root, text="Result:")
result_label.grid(row=4, column=0, columnspan=2, pady=10)

# Start the GUI event loop
root.mainloop()
