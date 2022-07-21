# Make a clock using Python programming language

from tkinter import *
from tkinter.ttk import *

from time import strftime

root = Tk()
root.title("Classic Clock")

def time():
    # For 24 hours functionality
    # string = strftime('%H:%M:%S %p')
    # For 12 hours functionality
    string = strftime('%I:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)


label = Label(root, font=("ds-digital", 100), background="black", foreground="cyan")
label.pack(anchor="center")


time()
mainloop()
