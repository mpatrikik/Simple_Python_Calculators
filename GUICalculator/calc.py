import tkinter as tk
from tkinter import ttk  # Import themed Tkinter
from tkinter import messagebox

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        screen_width = master.winfo_screenwidth()
        screen_height = master.winfo_screenheight()

        window_width = 300
        window_height = 400

        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        master.geometry(f"{window_width}x{window_height}+{x}+{y}")
        master.resizable(False, False)

        self.style = ttk.Style()
        self.style.theme_use("clam")  # or "alt", "default", "classic" - experiment!
        self.style.configure("TButton", font=("Arial", 16), padding=6)
        self.style.configure("TLabel", font=("Arial", 20), padding=4, background="#f0f0f5") # Light gray background
        self.style.configure("Display.TLabel", font=("Arial", 30), padding=8, anchor="e", background="#ffffff") # White background for display

        self.display_var = tk.StringVar(value="0")
        self.expression = ""

        self.create_widgets()

    def create_widgets(self):
        # Display
        self.display_label = ttk.Label(self.master, textvariable=self.display_var, style="Display.TLabel")
        self.display_label.grid(row=0, column=0, columnspan=4, sticky="nsew", pady=(0, 10))

        # Buttons
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
            ('C', 5, 0), ('√', 5, 1), ('^2', 5, 2)
        ]

        for button_text, row, col in buttons:
            command = lambda t=button_text: self.button_clicked(t)
            button = ttk.Button(self.master, text=button_text, command=command)
            button.grid(row=row, column=col, sticky="nsew", padx=2, pady=2)

        for i in range(6): # 6 rows including display
            self.master.grid_rowconfigure(i, weight=1)
        for i in range(4):  # 4 columns
            self.master.grid_columnconfigure(i, weight=1)

    def button_clicked(self, text):
        if text == "=":
            self.calculate()
        elif text == "C":
            self.clear()
        elif text == "√":
            self.square_root()
        elif text == "^2":
            self.square()
        else:
            self.append_to_expression(text)

    def calculate(self):
        try:
            # Evaluate the expression and update the display
            result = str(eval(self.expression))
            self.display_var.set(result)
            self.expression = result # Keep result for further calculations
        except (SyntaxError, ZeroDivisionError, NameError) as e:  # Catch specific errors
            messagebox.showerror("Error", "Invalid Expression")
            self.clear()
        except Exception as e: # Catch all other errors
            messagebox.showerror("Error", f"An unexpected error occurred: {e}")
            self.clear()


    def clear(self):
        self.expression = ""
        self.display_var.set("0")

    def square_root(self):
        try:
            if self.expression: #Added condition
                result = str(eval(self.expression + "**0.5"))
                self.display_var.set(result)
                self.expression = result  # Chain operations
            else: #Added else
                self.display_var.set("0") #Set 0

        except Exception as e:
            messagebox.showerror("Error", "Invalid Expression")
            self.clear()

    def square(self):
        try:
            if self.expression: #Added condition
                result = str(eval(self.expression + "**2"))
                self.display_var.set(result)
                self.expression = result  # Chain operations
            else: #Added else
                self.display_var.set("0")
        except Exception as e:
            messagebox.showerror("Error", "Invalid Expression")
            self.clear()

    def append_to_expression(self, text):
        self.expression += text
        self.display_var.set(self.expression)



root = tk.Tk()
calculator = Calculator(root)
root.mainloop()