# =============================== Sahar ex10 =============================== #
from tkinter import *


def click(event):
    convert(textbox.get())


def convert(cel):
    celsius = int(cel)
    fahrenheit = 9.0 / 5.0 * (celsius + 32)
    display_text.set(fahrenheit)


root = Tk()
root.geometry("500x500")
my_label = Label(root, text="Fahrenheit to celsius converter")
my_label.pack()
textbox = Entry(root)
textbox.pack()
btn = Button(root, text="Convert!", cursor='hand2')
btn.pack()
display_text = StringVar()
txt = Label(root, textvariable=display_text)
txt.pack()
btn.bind("<Button-1>", click)
root.mainloop()

