from tkinter import *
from tkinter import ttk



def edit(event):
    box.config(state="disabled")  
    box.config(cursor="plus")
def insert(event):
    box.config(state="normal")  
def select(event):
    box.tag_add("hello","1.00", "1.10")
    box.tag_config("hello", background="white")
root = Tk()

root.title("Notebook")

box = Text(root, height=50, width=50, bg="black", fg="alice blue", relief=SUNKEN
    

           )
box.pack(padx = 5, pady = 5)


root.bind('<Escape>', edit)
root.bind('<Escape>', select)
root.bind('<i>', insert)

root.mainloop()
