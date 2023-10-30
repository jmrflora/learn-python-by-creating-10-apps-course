import tkinter as tk
from tkinter import ttk

# setup
window = tk.Tk()
window.title('buttons')
window.geometry('600x400')

# button
def button_func():
	print('a basic button')
	print(radio_var.get())

button_string = tk.StringVar(value = 'A button with string var')
button = ttk.Button(window, text = 'A simple button', command = button_func, textvariable = button_string)
button.pack()

# checkbutton
check_var = tk.IntVar(value = 10)
check1 = ttk.Checkbutton(
	window, 
	text = 'checkbox 1', 
	command = lambda: print(check_var.get()),
	variable = check_var,
	onvalue = 10,
	offvalue = 5)
check1.pack()

check2 = ttk.Checkbutton(
	window, 
	text = 'Checkbox 2',
	command = lambda: check_var.set(5))
check2.pack()

# radio buttons
radio_var = tk.StringVar()
radio1 = ttk.Radiobutton(
	window, 
	text = 'Radiobutton 1', 
	value = 1, 
	variable = radio_var,
	command = lambda: print(radio_var.get()))
radio1.pack()

radio2 = ttk.Radiobutton(window, text = 'Radiobutton 2', value = 1, variable = radio_var)
radio2.pack()

# create another checkbutton and 2 radiobuttons 
# radio button:
	# values for the buttons are A and B
	# ticking either prints the value of the checkbutton
	# ticking the radio button unchecks the checkbutton
# check button: 
	# ticking the checkbutton prints the value of the radio button value 
	# use tkinter var for Booleans! 

# exercise radios 

def exercise_radio_func():
    print(exercise_check_var.get())
    exercise_check_var.set(False)

def exercise_check_func():
    print(exercise_radio_var.get())   

exercise_radio_var = tk.StringVar()

exercise_radio1 = ttk.Radiobutton(master=window, value='A', variable= exercise_radio_var, command=exercise_radio_func)
exercise_radio2 = ttk.Radiobutton(master=window, value="B", variable= exercise_radio_var, command=exercise_radio_func)

exercise_check_var = tk.BooleanVar()
exercise_check = ttk.Checkbutton(master=window, text= 'checkbox exercise', variable=exercise_check_var, onvalue=True, offvalue=False, command=exercise_check_func)

exercise_radio1.pack()
exercise_radio2.pack()
exercise_check.pack()

# run 
window.mainloop()