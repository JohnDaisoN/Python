import tkinter


def add():
    num1 = float(num1_entry.get())
    num2 = float(num2_entry.get())
    result = num1 + num2
    result_label.config(text=result)

def sub():
    num1 = float(num1_entry.get())
    num2 = float(num2_entry.get())
    result = num1 - num2
    result_label.config(text=result)

def multiply():
    num1 = float(num1_entry.get())
    num2 = float(num2_entry.get())
    result = num1 * num2
    result_label.config(text=result)

def divide():
    num1 = float(num1_entry.get())
    num2 = float(num2_entry.get())
    result = num1 / num2
    result_label.config(text=result)


# create the main window
root = tkinter.Tk()
root.title("Calculator")
# create the widgets
num1_label = tkinter.Label(root, text="Number 1:")
num1_entry = tkinter.Entry(root)
num2_label = tkinter.Label(root, text="Number 2:")
num2_entry = tkinter.Entry(root)
add_button = tkinter.Button(root, text="Add", command=add)
sub_button = tkinter.Button(root, text="Subtract", command=sub)
mult_button = tkinter.Button(root, text="Multiply", command=multiply)
div_button = tkinter.Button(root, text="Divide", command=divide)
result_label = tkinter.Label(root, text="Result:")
# layout the widgets
num1_label.grid(row=0, column=0, sticky="e")
num1_entry.grid(row=0, column=1)
num2_label.grid(row=1, column=0, sticky="e")
num2_entry.grid(row=1, column=1)
add_button.grid(row=2, column=0, columnspan=2, pady=10)
sub_button.grid(row=2, column=2, columnspan=2, pady=10)
mult_button.grid(row=2, column=4, columnspan=2, pady=10)
div_button.grid(row=2, column=6, columnspan=2, pady=10)
result_label.grid(row=3, column=0, columnspan=2)

# run the main loop
root.mainloop()