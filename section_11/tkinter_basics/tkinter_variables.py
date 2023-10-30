import tkinter as tk
from tkinter import ttk

window = tk.Tk()

def button_func():
    print(string_var.get())
    string_var.set('button pressed')

string_var = tk.StringVar()

label = ttk.Label(master= window, text= "label", textvariable= string_var)
label.pack()

entry = ttk.Entry(master = window, textvariable = string_var)
entry.pack()

button = ttk.Button(master= window, text="button", command= button_func)
button.pack()


window.mainloop()