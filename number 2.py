from tkinter import *

win = Tk()

win.geometry("400x150")
win.title("Text Field")

txt = Entry(win, border= 3)
txt.place(x = 130, y=50)

win.mainloop()