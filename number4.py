import tkinter as tk
import random

def change_color():

    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = f"#{r:02x}{g:02x}{b:02x}"
    button1.configure(bg=color)

window = tk.Tk()

window.title("Button")
window.geometry("500x200")

button1 = tk.Button(window, text="color", command=change_color)
button1.place(x=90, y=50)

button2 = tk.Button(window, text="<--- CLICK TO CHANGE THE COLOR OF THE BUTTON", command=change_color)
button2.place(x=130,y=50)

window.mainloop()