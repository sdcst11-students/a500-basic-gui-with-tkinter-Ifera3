#!python3
import tkinter as tk

window = tk.Tk()
window.title('Example')
window.geometry('257x136')
window.configure(bg='#FFFFFF')

dog = tk.PhotoImage(file='dog.png')
dogplace = tk.Label(window, image=dog, bg='#FFFFFF')
text1 = tk.Label(window, text='Pochacco!', bg='#FFFFFF')
text2 = tk.Label(window, text='A cuddly litle Puppy! This is from the same\ncreators who brought you Keropi and Kero Kero', bg='#81FFFD')

dogplace.place(x=65, y=0)
text1.place(x=135, y=45)
text2.place(x=0, y=100)

window.mainloop()