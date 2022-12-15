import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

root = tk.Tk()
root.title("Treeview demo")
root.geometry("500x195")

columns = ('first_name', 'last_name', 'email')
tree = ttk.Treeview(root, columns=columns, show='headings')

tree.heading('first_name', text='first name')
tree.heading('last_name', text='last name')
tree.heading('email', text='email')

contacts = []

for n in range(1, 100):
    contacts.append((f'first {n}', f'last {n}', f'email{n}@example.com'))

for contact in contacts:
    tree.insert('', tk.END, values=contact)

def item_selected(event):
    for selected_item in tree.selection():
        item = tree.item(selected_item)
        record = item['value']

        showinfo(title='Information', message=','.join(record))
    

tree.bind('<<TreeviewSelect>>', item_selected)

tree.grid(row=0, column=0, sticky='nsew')

scrollbar = ttk.Scrollbar(root, orient=tk.VERTICAL, command=tree.yview)

tree.configure(yscroll=scrollbar.set)
scrollbar.grid(row=0, column=1, sticky='ns')

root.mainloop()