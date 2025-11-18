from tkinter import *
from tkinter import ttk



def toString(floater):
    return str(floater)



def select(cur):
    word = cur.split(".")
    beg = word[0]
    end = word[1]
    digit = int(word[1])
    digit += 1
    print(beg + "." + str(digit))
    print(cur)
    

    
    # box.tag_add("hello",cur, beg + ".0" + str(digit) )
    box.tag_add("hello","1.4","1.6") 
    box.tag_config("hello", underline=1)

def edit(event):
    box.config(state="disabled")  
    box.config(cursor="plus")
    cur = box.index('current')
    select(cur)
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
