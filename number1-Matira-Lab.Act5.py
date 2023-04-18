import tkinter as tk

wi = tk.Tk()

wi.title("Laboratory Activity 5")

wi.geometry("400x100")

t_label = tk.Label(wi, text="Submitted to: Mam Sayo")
t_label.pack(side=tk.BOTTOM)

s_label = tk.Label(wi, text="Laboratory Activity 5")
s_label.pack(side=tk.BOTTOM)

wi.mainloop()