from tkinter import *
from tkinter import ttk

root = Tk()

my_frame = ttk.Frame(root, padding=100, width=700, height=250)
my_frame.pack()

ttk.Label(my_frame, text='FirstName').grid(column=0, row=0)
ttk.Label(my_frame, text='Last Name').grid(column=0, row=1)
ttk.Entry(my_frame).grid(row=0, column=1)
ttk.Entry(my_frame).grid(row=1, column=1)
ttk.Button(my_frame, text="Quit", command=root.destroy).grid(column=0, row=2, columnspan=2)

root.mainloop()