import tkinter as tk
from tkinter import messagebox, simpledialog
import json

# Contact book dictionary to store contacts
contact_book = {}

# Function to add a new contact
def add_contact():
    name = entry_name.get()
    phone = entry_phone.get()
    email = entry_email.get()
    address = entry_address.get()
    
    if name and phone:
        contact_book[name] = {'Phone': phone, 'Email': email, 'Address': address}
        messagebox.showinfo("Success", "Contact added successfully!")
        clear_entries()
        update_contact_list()
    else:
        messagebox.showerror("Error", "Name and phone number are required!")

# Function to clear the input fields
def clear_entries():
    entry_name.delete(0, tk.END)
    entry_phone.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_address.delete(0, tk.END)

# Function to update the displayed contact list
def update_contact_list():
    listbox_contacts.delete(0, tk.END)
    for name, details in contact_book.items():
        listbox_contacts.insert(tk.END, f"{name} - {details['Phone']}")

# Function to view contact details when selected from the list
def view_contact():
    try:
        selected_contact = listbox_contacts.get(listbox_contacts.curselection())
        contact_name = selected_contact.split(" - ")[0]
        contact = contact_book.get(contact_name)
        if contact:
            messagebox.showinfo("Contact Details",
                                f"Name: {contact_name}\nPhone: {contact['Phone']}\nEmail: {contact['Email']}\nAddress: {contact['Address']}")
    except:
        messagebox.showerror("Error", "Please select a contact to view")

# Function to search for a contact by name or phone
def search_contact():
    query = entry_search.get().strip().lower()
    if query:
        for name, details in contact_book.items():
            if query in name.lower() or query in details['Phone']:
                messagebox.showinfo("Search Result", f"Name: {name}\nPhone: {details['Phone']}\nEmail: {details['Email']}\nAddress: {details['Address']}")
                return
        messagebox.showwarning("Not Found", "No contact found with the given name or phone number!")
    else:
        messagebox.showwarning("Input Required", "Please enter a name or phone number to search!")

# Function to update a contact's details
def update_contact():
    try:
        selected_contact = listbox_contacts.get(listbox_contacts.curselection())
        contact_name = selected_contact.split(" - ")[0]
        if contact_name in contact_book:
            new_phone = simpledialog.askstring("Update Phone", "Enter new phone number:", initialvalue=contact_book[contact_name]['Phone'])
            new_email = simpledialog.askstring("Update Email", "Enter new email address:", initialvalue=contact_book[contact_name]['Email'])
            new_address = simpledialog.askstring("Update Address", "Enter new address:", initialvalue=contact_book[contact_name]['Address'])
            if new_phone:
                contact_book[contact_name]['Phone'] = new_phone
            contact_book[contact_name]['Email'] = new_email if new_email else ""
            contact_book[contact_name]['Address'] = new_address if new_address else ""
            update_contact_list()
            messagebox.showinfo("Success", "Contact updated successfully!")
        else:
            messagebox.showerror("Error", "Contact not found!")
    except:
        messagebox.showerror("Error", "Please select a contact to update!")

# Function to delete a contact
def delete_contact():
    try:
        selected_contact = listbox_contacts.get(listbox_contacts.curselection())
        contact_name = selected_contact.split(" - ")[0]
        if contact_name in contact_book:
            del contact_book[contact_name]
            update_contact_list()
            messagebox.showinfo("Success", "Contact deleted successfully!")
        else:
            messagebox.showerror("Error", "Contact not found!")
    except:
        messagebox.showerror("Error", "Please select a contact to delete!")

# Function to save the contacts to a JSON file
def save_contacts():
    with open("contacts.json", "w") as file:
        json.dump(contact_book, file)
    messagebox.showinfo("Success", "Contacts saved to contacts.json!")

# Function to load contacts from a JSON file
def load_contacts():
    global contact_book
    try:
        with open("contacts.json", "r") as file:
            contact_book = json.load(file)
        update_contact_list()
    except FileNotFoundError:
        messagebox.showwarning("File Not Found", "No saved contacts found!")
    except json.JSONDecodeError:
        messagebox.showerror("Error", "Failed to load contacts!")

# Create the main window
root = tk.Tk()
root.title("Contact Book")

# Input fields for adding contacts
label_name = tk.Label(root, text="Name:")
label_name.grid(row=0, column=0, padx=10, pady=10)

entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1, padx=10, pady=10)

label_phone = tk.Label(root, text="Phone:")
label_phone.grid(row=1, column=0, padx=10, pady=10)

entry_phone = tk.Entry(root)
entry_phone.grid(row=1, column=1, padx=10, pady=10)

label_email = tk.Label(root, text="Email:")
label_email.grid(row=2, column=0, padx=10, pady=10)

entry_email = tk.Entry(root)
entry_email.grid(row=2, column=1, padx=10, pady=10)

label_address = tk.Label(root, text="Address:")
label_address.grid(row=3, column=0, padx=10, pady=10)

entry_address = tk.Entry(root)
entry_address.grid(row=3, column=1, padx=10, pady=10)

# Buttons to add, view, update, and delete contacts
add_button = tk.Button(root, text="Add Contact", command=add_contact)
add_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

view_button = tk.Button(root, text="View Contact", command=view_contact)
view_button.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

update_button = tk.Button(root, text="Update Contact", command=update_contact)
update_button.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

delete_button = tk.Button(root, text="Delete Contact", command=delete_contact)
delete_button.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

# Listbox to display all contacts
listbox_contacts = tk.Listbox(root, width=40)
listbox_contacts.grid(row=0, column=2, rowspan=6, padx=10, pady=10)

# Search functionality
label_search = tk.Label(root, text="Search by Name/Phone:")
label_search.grid(row=8, column=0, padx=10, pady=10)

entry_search = tk.Entry(root)
entry_search.grid(row=8, column=1, padx=10, pady=10)

search_button = tk.Button(root, text="Search", command=search_contact)
search_button.grid(row=8, column=2, padx=10, pady=10)

# Save and load buttons for contact persistence
save_button = tk.Button(root, text="Save Contacts", command=save_contacts)
save_button.grid(row=9, column=0, padx=10, pady=10)

load_button = tk.Button(root, text="Load Contacts", command=load_contacts)
load_button.grid(row=9, column=1, padx=10, pady=10)

# Start the GUI event loop
root.mainloop()
