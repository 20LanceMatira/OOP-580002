import tkinter as tk

window = tk.Tk()
window.title("Laboratory Activity No.6")


instructions_label = tk.Label(window, text="Click the button to calculate the squares and cubes of numbers up to 10")
instructions_label.pack()


def calculate_squares_and_cubes():
    output_text.delete('1.0', tk.END)
    output_text.insert(tk.END, "Number\tSquare\tCube\n")

    for i in range(1, 11):
        square = i ** 2
        cube = i ** 3
        output_text.insert(tk.END, f"{i}\t{square}\t{cube}\n")
calculate_button = tk.Button(window, text="Calculate", command=calculate_squares_and_cubes)
calculate_button.pack()


output_text = tk.Text(window)
output_text.pack()


window.mainloop()






