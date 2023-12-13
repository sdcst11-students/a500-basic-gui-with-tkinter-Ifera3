#!python3
import tkinter as tk

window = tk.Tk()
window.title('Example')
window.configure(bg='#FFFFFF')

dog = tk.PhotoImage(file='dog.png')
dogplace = tk.Label(window, image=dog, bg='#FFFFFF')
text1 = tk.Label(window, text='Pochacco!', bg='#FFFFFF')
space1 = tk.Label(window, width=8, bg='#FFFFFF')
space2 = tk.Label(window, width=8, bg='#FFFFFF')
text2 = tk.Label(window, text='A cuddly litle Puppy! This is from the same\ncreators who brought you Keropi and Kero Kero', bg='#81FFFD')

space1.grid(row=1,column=1)
dogplace.grid(row=1,column=2)
text1.grid(row=1,column=3)
space2.grid(row=1,column=4)
text2.grid(row=2, column=1, columnspan=4)

window.mainloop()