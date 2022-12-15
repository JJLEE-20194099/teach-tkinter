from tkinter import *

root = Tk()
root.geometry("200x200")

options = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday"
]

clicked = StringVar()

clicked.set("Text is too long")

drop = OptionMenu(root, clicked, *options)
drop.config(width=20, anchor='w', padx=10, pady=20, highlightthickness=0)
drop.pack()

button = Button(master=root, text="click me", command=lambda: label.config(text = clicked.get()))
button.pack()

label = Label(root, text = "")
label.pack()

root.mainloop()