from tkinter import *
from tkinter import ttk


def select():
    box.tag_add("hello","1.00", "1.10")
    box.tag_config("hello", background="white")

def edit(event):
    select()
    box.config(state="disabled")  
    box.config(cursor="plus")
    print(box.index('current'))
def insert(event):
    box.config(state="normal")  
root = Tk()

root.title("Notebook")

box = Text(root, height=50, width=50, bg="black", fg="alice blue", relief=SUNKEN
    

           )
box.pack(padx = 5, pady = 5)


root.bind('<Escape>', edit)
root.bind('<i>', insert)

root.mainloop()
