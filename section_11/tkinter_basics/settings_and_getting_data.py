import tkinter as tk
from tkinter import ttk

def button_func():
    entry_text =entry.get()

    label['text'] = entry_text
    entry['state'] = 'disabled' 

def button2_func():
    label['text'] = "some text"
    entry['state'] = 'enabled'

window = tk.Tk()
window.title("Getting and setting widgets")

label = ttk.Label(master= window, text= "some text")
label.pack()

entry = ttk.Entry(master=window)
entry.pack()

button = ttk.Button(master= window, text = 'The button', command= button_func)
button.pack()

button2 = ttk.Button(master=window, text="the second button", command= button2_func)
button2.pack()

window.mainloop()