from tkinter import OUTSIDE
import tkinter
import tkinter.messagebox

root = tkinter.Tk()
root.geometry("1600x700")
def hello():
  tkinter.messagebox.showinfo("Hello DL", "Hello World")

b = tkinter.Button(root, text="Hello", command = hello)
b.pack()

b.place(x=100, y=100, height=100, width=100)
root.mainloop()