import tkinter as tk
from tkinter import messagebox
import math

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")
        master.geometry("400x600")  # Set a fixed size for the window

        # Entry widget for displaying calculations
        self.entry = tk.Entry(master, width=16, font=('Arial', 24), borderwidth=5, justify='right')
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # Creating buttons for the calculator
        self.create_buttons()

    def create_buttons(self):
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3),
            ('^', 5, 0), ('√', 5, 1)
        ]

        for (text, row, col) in buttons:
            button = tk.Button(self.master, text=text, width=5, height=2,
                               font=('Arial', 18), bg="#4CAF50", fg="white",
                               activebackground="#45a049",
                               command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col, padx=5, pady=5)

    def on_button_click(self, char):
        if char == 'C':
            self.entry.delete(0, tk.END)
        elif char == '=':
            self.calculate()
        else:
            self.entry.insert(tk.END, char)

    def calculate(self):
        try:
            expression = self.entry.get().replace('^', '**').replace('√', 'math.sqrt')
            result = eval(expression)
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, result)
        except Exception as e:
            messagebox.showerror("Error", "Invalid Input")

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()