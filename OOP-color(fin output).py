import tkinter as tk

class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        self.color_label = tk.Label(self.master, text="Click the buttons to display primary, secondary, and tertiary colors", font=("Arial", 14))
        self.color_label.grid(row=0, column=0, columnspan=3, pady=10)

        self.color_display = tk.Label(self.master, width=30, height=10)
        self.color_display.grid(row=1, column=1, pady=10)

        self.primary_button1 = tk.Button(self.master, text="Red", bg='red', command=lambda: self.set_color('red'))
        self.primary_button1.grid(row=2, column=0, pady=10, padx=10)
        self.primary_button1.bind("<Enter>", lambda e: self.set_color_text('Red'))

        self.primary_button2 = tk.Button(self.master, text="Yellow", bg='yellow', command=lambda: self.set_color('yellow'))
        self.primary_button2.grid(row=2, column=1, pady=10, padx=10)
        self.primary_button2.bind("<Enter>", lambda e: self.set_color_text('Yellow'))

        self.primary_button3 = tk.Button(self.master, text="Blue", bg='blue', command=lambda: self.set_color('blue'))
        self.primary_button3.grid(row=2, column=2, pady=10, padx=10)
        self.primary_button3.bind("<Enter>", lambda e: self.set_color_text('Blue'))

        self.secondary_button1 = tk.Button(self.master, text="Green", bg='green', command=lambda: self.set_color('green'))
        self.secondary_button1.grid(row=3, column=0, pady=10, padx=10)
        self.secondary_button1.bind("<Enter>", lambda e: self.set_color_text('Green'))

        self.secondary_button2 = tk.Button(self.master, text="Purple", bg='purple', command=lambda: self.set_color('purple'))
        self.secondary_button2.grid(row=3, column=1, pady=10, padx=10)
        self.secondary_button2.bind("<Enter>", lambda e: self.set_color_text('Purple'))

        self.secondary_button3 = tk.Button(self.master, text="Orange", bg='orange', command=lambda: self.set_color('orange'))
        self.secondary_button3.grid(row=3, column=2, pady=10, padx=10)
        self.secondary_button3.bind("<Enter>", lambda e: self.set_color_text('Orange'))

        self.tertiary_button1 = tk.Button(self.master, text="Magenta", bg='magenta', command=lambda: self.set_color('magenta'))
        self.tertiary_button1.grid(row=4, column=0, pady=10, padx=10)
        self.tertiary_button1.bind("<Enter>", lambda e: self.set_color_text('Magenta'))

        self.tertiary_button2 = tk.Button(self.master, text="Cyan", bg='cyan', command=lambda: self.set_color('cyan'))
        self.tertiary_button2.grid(row=4, column=1, pady=10, padx=10)
        self.tertiary_button2.bind("<Enter>", lambda e: self.set_color_text('Cyan'))

        self.tertiary_button3= tk.Button(self.master, text="Purple", bg='purple', command=lambda: self.set_color('purple'))
        self.tertiary_button3.grid(row=4, column=2, pady=10, padx=10)
        self.tertiary_button3.bind("<Enter>", lambda e: self.set_color_text('Purple'))

        self.color_text = tk.Label(self.master, text="", font=("Arial", 14))
        self.color_text.grid(row=4, column=3, pady=10)

    def set_color(self, color):
        self.color_display.configure(bg=color)

    def set_color_text(self, text):
        self.color_text.configure(text=text)

root = tk.Tk()
app = App(root)
app.mainloop()