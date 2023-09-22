import tkinter as tk
#from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    mile_input = entryInt.get()
    km_output = mile_input * 1.61 
    output_string.set(km_output) 

window = ttk.Window(themename= 'darkly') 
window.title('Demo')
window.geometry('300x150')

title_label = ttk.Label(master= window, text= 'Miles to Kilometers', font= 'Calibri 24 bold')
title_label.pack()

input_frame = ttk.Frame(master= window)
entryInt = tk.IntVar()
entry = ttk.Entry(master=input_frame, textvariable= entryInt)

button = ttk.Button(master=input_frame, text='Convert', command= convert)
entry.pack(side='left', padx= 10)
button.pack(side='left')
input_frame.pack(pady =10)

output_string = tk.StringVar()
output = ttk.Label(master=window, text= 'Output', font= 'Calibri 24',
                   textvariable= output_string)
output.pack(pady = 5)

window.mainloop()