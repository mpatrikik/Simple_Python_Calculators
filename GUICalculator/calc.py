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

        self.expression = ""
        self.result = ""

        self.create_widgets()

    def create_widgets(self):
        # Display
        self.display_label = ttk.Label(self.master, textvariable=tk.StringVar(value="0"), style="Display.TLabel")
        self.display_label.grid(row=0, column=0, columnspan=4, sticky="nsew", pady=(0, 10))

        # Buttons
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+',
            'C', '√', '^2'
        ]

        row, col = 1, 0
        for button_text in buttons:
            command = lambda text=button_text: self.button_clicked(text)
            button = ttk.Button(self.master, text=button_text, command=command)
            button.grid(row=row, column=col, sticky="nsew", padx=2, pady=2)
            col += 1
            if col > 3:
                col = 0
                row += 1

        for i in range(5):  # 5 rows
            self.master.grid_rowconfigure(i, weight=1)
        for i in range(4):  # 4 columns
            self.master.grid_columnconfigure(i, weight=1)

    def button_clicked(self, text):
        if text == "=":
            try:
                self.result = str(eval(self.expression))
                self.expression = "" # Clear for next calculation
                self.display_label.config(textvariable=tk.StringVar(value=self.result)) # Update display with result
            except Exception as e:
                messagebox.showerror("Error", "Invalid Expression")
                self.expression = ""
                self.display_label.config(textvariable=tk.StringVar(value="0")) # Reset to "0"
        elif text == "C":
            self.expression = ""
            self.result = ""
            self.display_label.config(textvariable=tk.StringVar(value="0")) # Reset to "0"
        elif text == "√":  # Square root
            try:
                self.result = str(eval(self.expression + "**0.5"))
                self.expression = ""
                self.display_label.config(textvariable=tk.StringVar(value=self.result))
            except Exception as e:
                messagebox.showerror("Error", "Invalid Expression")
                self.expression = ""
                self.display_label.config(textvariable=tk.StringVar(value="0"))
        elif text == "^2":  # Square
            try:
                self.result = str(eval(self.expression + "**2"))
                self.expression = ""
                self.display_label.config(textvariable=tk.StringVar(value=self.result))
            except Exception as e:
                messagebox.showerror("Error", "Invalid Expression")
                self.expression = ""
                self.display_label.config(textvariable=tk.StringVar(value="0"))
        else:
            self.expression += text
            self.display_label.config(textvariable=tk.StringVar(value=self.expression))


root = tk.Tk()
calculator = Calculator(root)
root.mainloop()