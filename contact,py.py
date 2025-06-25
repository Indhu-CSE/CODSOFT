import tkinter as tk
from tkinter import messagebox, simpledialog
import json
import os

contacts_file = "contacts.json"

# Load contacts from file
def load_contacts():
    if os.path.exists(contacts_file):
        with open(contacts_file, "r") as file:
            return json.load(file)
    return {}

# Save contacts to file
def save_contacts():
    with open(contacts_file, "w") as file:
        json.dump(contacts, file, indent=4)

# Add a new contact
def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()

    if name and phone:
        contacts[name] = {"Phone": phone, "Email": email, "Address": address}
        save_contacts()
        messagebox.showinfo("Success", "Contact added successfully!")
        clear_entries()
        view_contacts()
    else:
        messagebox.showwarning("Error", "Name and Phone are required.")

# View all contacts
def view_contacts():
    contact_list.delete(0, tk.END)
    for name, info in contacts.items():
        contact_list.insert(tk.END, f"{name} - {info['Phone']}")

# Search contact
def search_contact():
    query = simpledialog.askstring("Search", "Enter name or phone number:")
    if query:
        contact_list.delete(0, tk.END)
        for name, info in contacts.items():
            if query.lower() in name.lower() or query in info["Phone"]:
                contact_list.insert(tk.END, f"{name} - {info['Phone']}")

# Update selected contact
def update_contact():
    selected = contact_list.curselection()
    if selected:
        contact_name = contact_list.get(selected[0]).split(" - ")[0]
        phone = phone_entry.get()
        email = email_entry.get()
        address = address_entry.get()
        contacts[contact_name] = {"Phone": phone, "Email": email, "Address": address}
        save_contacts()
        messagebox.showinfo("Success", "Contact updated.")
        view_contacts()
    else:
        messagebox.showwarning("Error", "No contact selected.")

# Delete selected contact
def delete_contact():
    selected = contact_list.curselection()
    if selected:
        contact_name = contact_list.get(selected[0]).split(" - ")[0]
        confirm = messagebox.askyesno("Confirm", f"Delete {contact_name}?")
        if confirm:
            del contacts[contact_name]
            save_contacts()
            view_contacts()

# Populate fields when contact is selected
def load_selected_contact(event):
    selected = contact_list.curselection()
    if selected:
        contact_name = contact_list.get(selected[0]).split(" - ")[0]
        info = contacts[contact_name]
        name_entry.delete(0, tk.END)
        name_entry.insert(0, contact_name)
        phone_entry.delete(0, tk.END)
        phone_entry.insert(0, info["Phone"])
        email_entry.delete(0, tk.END)
        email_entry.insert(0, info["Email"])
        address_entry.delete(0, tk.END)
        address_entry.insert(0, info["Address"])

# Clear entry fields
def clear_entries():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)

# Main Window
root = tk.Tk()
root.title("Contact Book")

contacts = load_contacts()

# Labels & Entry
tk.Label(root, text="Name").grid(row=0, column=0)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1)

tk.Label(root, text="Phone").grid(row=1, column=0)
phone_entry = tk.Entry(root)
phone_entry.grid(row=1, column=1)

tk.Label(root, text="Email").grid(row=2, column=0)
email_entry = tk.Entry(root)
email_entry.grid(row=2, column=1)

tk.Label(root, text="Address").grid(row=3, column=0)
address_entry = tk.Entry(root)
address_entry.grid(row=3, column=1)

# Buttons
tk.Button(root, text="Add", command=add_contact).grid(row=4, column=0)
tk.Button(root, text="Update", command=update_contact).grid(row=4, column=1)
tk.Button(root, text="Delete", command=delete_contact).grid(row=5, column=0)
tk.Button(root, text="Search", command=search_contact).grid(row=5, column=1)
tk.Button(root, text="View All", command=view_contacts).grid(row=6, column=0, columnspan=2)

# Listbox
contact_list = tk.Listbox(root, width=50)
contact_list.grid(row=7, column=0, columnspan=2)
contact_list.bind('<<ListboxSelect>>', load_selected_contact)

view_contacts()
root.mainloop()
