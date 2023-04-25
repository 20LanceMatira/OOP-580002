from tkinter import *


def button_click(number):
    entry.insert(END, str(number))


def button_add():
    global f_num
    f_num = float(entry.get())
    entry.delete(0, END)
    global math
    math = "addition"


def button_subtract():
    global f_num
    f_num = float(entry.get())
    entry.delete(0, END)
    global math
    math = "subtraction"


def button_multiply():
    global f_num
    f_num = float(entry.get())
    entry.delete(0, END)
    global math
    math = "multiplication"


def button_divide():
    global f_num
    f_num = float(entry.get())
    entry.delete(0, END)
    global math
    math = "division"

def button_equal():
    second_num = float(entry.get())
    entry.delete(0, END)
    if math == "addition":
        entry.insert(0, f_num + second_num)
    elif math == "subtraction":
        entry.insert(0, f_num - second_num)
    elif math == "multiplication":
        entry.insert(0, f_num * second_num)
    elif math == "division":
        entry.insert(0, f_num / second_num)

def button_clear():
    entry.delete(0, END)

window = Tk()
window.title("Calculator")


entry = Entry(window, width=40, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)


for i in range(0, 10):
    button = Button(window, text=str(i), padx=40, pady=20, command=lambda num=i: button_click(num))
    button.grid(row=((9 - i) // 3) + 1, column=(i % 3))

button_add = Button(window, text="+", padx=39, pady=20, command=button_add)
button_add.grid(row=4, column=0)
button_subtract = Button(window, text="-", padx=41, pady=20, command=button_subtract)
button_subtract.grid(row=5, column=0)
button_multiply = Button(window, text="*", padx=40, pady=20, command=button_multiply)
button_multiply.grid(row=5, column=1)
button_divide = Button(window, text="/", padx=41, pady=20, command=button_divide)
button_divide.grid(row=5, column=2)
button_equal = Button(window, text="=", padx=91, pady=20, command=button_equal)
button_equal.grid(row=4, column=1, columnspan=2)
button_clear = Button(window, text="Clear", padx=79, pady=20, command=button_clear)
button_clear.grid(row=6, column=0, columnspan=3)

window.bind("<Return>", lambda event: button_equal())
window.bind("<KP_Enter>", lambda event: button_equal())
window.bind("<Escape>", lambda event: button_clear())

window.mainloop()
