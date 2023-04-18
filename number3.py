import tkinter as tk

window = tk.Tk()

window.title("Father of Computer")

window.geometry("400x150")

label = tk.Label(window, text="Charles Babbage", bg="cyan", fg="black", font=("Arial", 24))
label.place(x=80, y=50)

window.mainloop()