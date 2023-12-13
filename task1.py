#!python3
import tkinter as tk

window = tk.Tk()
window.title('tk')

entery1 = tk.Entry(window,text='')
lable = tk.Label(window,text="x")
entery2 = tk.Entry(window)
button1 = tk.Button(window,text='=', border=1)
entery3 = tk.Entry(window)

entery1.grid(row=1, column=1, padx= 2)
lable.grid(row=1, column=2, padx= 2)
entery2.grid(row=1, column=3, padx= 2)
button1.grid(row=1, column=4, padx= 2)
entery3.grid(row=1, column=5, padx= 2)

window.mainloop()