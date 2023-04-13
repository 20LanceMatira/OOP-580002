import tkinter as tk

import tkinter as tk

window = tk.Tk()
window.geometry("600x450")
window.title("Full Name")

label1 = tk.Label(window, text=" Enter Given Name:")
label1.grid(row=0, column=0, padx=30, pady=30)

entry1 = tk.Entry(window)
entry1.grid(row=0, column=1, padx=30, pady=30)

label2 = tk.Label(window, text=" Enter Middle Name:")
label2.grid(row=1, column=0, padx=30, pady=30)

entry2 = tk.Entry(window)
entry2.grid(row=1, column=1, padx=30, pady=30)

label3 = tk.Label(window, text=" Enter Last Name:")
label3.grid(row=2, column=0, padx=30, pady=30)

entry3 = tk.Entry(window)
entry3.grid(row=2, column=1, padx=30, pady=30)

entry4 = tk.Entry(window)
entry4.grid(row=3, column=1, padx=30, pady=30)

def full_name():
    fullname = entry1.get() + " " + entry2.get() + " " + entry3.get()
    entry4.delete(0, tk.END)
    entry4.insert(0, fullname)

def clear():
    clearname = entry1.get() + " " + entry2.get() + " " + entry3.get()
    entry4.delete(0, tk.END)
    entry4.insert(0, clearname)

button = tk.Button(window, text="Show Full Name", command=full_name)
button.grid(row=3, column=0, padx=30, pady=30)
button = tk.Button(window, text="clear all", command=clear)
button.grid(row=4, column=0, padx=30, pady=30)


window.mainloop()








