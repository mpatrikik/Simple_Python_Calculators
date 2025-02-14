import tkinter as tk

LARGE_FONT_STYLE = ("Arial", 40, "bold")
SMALL_FONT_STYLE = ("Arial", 16)
LIGHT_GRAY = "#F5F5F5"
LABEL_COLOR = "#25265E"


class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("375x667")
        self.window.resizable(0, 0)
        self.window.title("Calculator")
        self.center_window()

        self.total_expression = "0"
        self.current_expression = "0"
        self.display_frame = self.create_display_frame()

        self.total_label, self.label = self.create_display_labels()
        self.buttons_frame = self.create_display_frame()

    def create_display_labels(self):
        total_label = tk.Label(self.display_frame, text=self.total_expression, anchor=tk.E, bg=LIGHT_GRAY, fg=LABEL_COLOR, padx=24, font=SMALL_FONT_STYLE)
        total_label.pack(expand=True, fill='both')

        label = tk.Label(self.display_frame, text=self.current_expression, anchor=tk.E, bg=LIGHT_GRAY, fg=LABEL_COLOR, padx=24, font=LARGE_FONT_STYLE)
        label.pack(expand=True, fill='both')

        return total_label, label

    # centering the window
    def center_window(self):
        window_width = 375
        window_height = 667
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        position_top = int(screen_height / 2 - window_height / 2)
        position_right = int(screen_width / 2 - window_width / 2)
        self.window.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')

    def create_display_frame(self):
        frame = tk.Frame(self.window, height=221, bg=LIGHT_GRAY)
        frame.pack(expand=True, fill="both")
        return frame

    def create_buttons_frame(self):
        frame = tk.Frame(self.window)
        frame.pack(expand=True, fill="both")
        return frame


    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    calc = Calculator()
    calc.run()
