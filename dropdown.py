from tkinter import *

root = Tk()
root.geometry("200x200")

def show():
    label.config(text = clicked.get())

options = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday"
]

clicked = StringVar()

clicked.set("Monday")

drop = OptionMenu(root, clicked, *options)
drop.pack()

button = Button(master=root, text="click me", command=show)
button.pack()

label = Label(root, text = "")
label.pack()

root.mainloop()