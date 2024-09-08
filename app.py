import tkinter as tk
from tkinter import messagebox
import math

class GlassButton(tk.Button):
    def __init__(self, parent, text, **kwargs):
        super().__init__(parent, text=text, **kwargs)
        self.configure(bg='#B0BEC5', fg='#FFFFFF', relief=tk.FLAT, bd=0, font=("Arial", 18))

    def on_enter(self, event):
        self.configure(bg='#90A4AE')

    def on_leave(self, event):
        self.configure(bg='#B0BEC5')

class FinancialCalculator(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.create_widgets()

    def create_widgets(self):
        # Display entry
        self.result_var = tk.StringVar()
        display = tk.Entry(self, textvariable=self.result_var, font=("Arial", 24), bd=10, relief=tk.FLAT, justify='right', bg='#CFD8DC', fg='#000000')
        display.grid(row=0, column=0, columnspan=4, sticky='nsew')

        # Button definitions for financial operations
        financial_buttons = [
            ('PV', 1, 0), ('FV', 1, 1), ('PMT', 1, 2), ('AMT', 1, 3)
        ]

        for (text, row, column) in financial_buttons:
            button = GlassButton(self, text=text, command=lambda t=text: self.on_button_click(t))
            button.grid(row=row + 1, column=column, sticky='nsew', padx=5, pady=5)
            button.bind("<Enter>", button.on_enter)
            button.bind("<Leave>", button.on_leave)

        # Configure rows and columns
        for i in range(3):
            self.grid_rowconfigure(i, weight=1)
        for i in range(4):
            self.grid_columnconfigure(i, weight=1)

    def on_button_click(self, button_text):
        current_text = self.result_var.get()
        if button_text == 'PV':
            self.result_var.set("Present Value (rate, nper, pmt)")
        elif button_text == 'FV':
            self.result_var.set("Future Value (rate, nper, pmt)")
        elif button_text == 'PMT':
            self.result_var.set("Payment (rate, nper, pv)")
        elif button_text == 'AMT':
            self.result_var.set("Amortization (principal, rate, nper)")

class ScientificCalculator(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.create_widgets()

    def create_widgets(self):
        # Display entry
        self.result_var = tk.StringVar()
        display = tk.Entry(self, textvariable=self.result_var, font=("Arial", 24), bd=10, relief=tk.FLAT, justify='right', bg='#CFD8DC', fg='#000000')
        display.grid(row=0, column=0, columnspan=6, sticky='nsew')

        # Button definitions for scientific operations
        scientific_buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
            ('sqrt', 5, 0), ('^2', 5, 1), ('exp', 5, 2), ('!', 5, 3),
            ('sin', 6, 0), ('cos', 6, 1), ('tan', 6, 2), ('deg', 6, 3),
            ('rad', 7, 0), ('asin', 7, 1), ('acos', 7, 2), ('atan', 7, 3),
            ('abs', 8, 0), ('sinh', 8, 1), ('cosh', 8, 2), ('tanh', 8, 3)
        ]

        for (text, row, column) in scientific_buttons:
            button = GlassButton(self, text=text, command=lambda t=text: self.on_button_click(t))
            button.grid(row=row + 1, column=column, sticky='nsew', padx=5, pady=5)
            button.bind("<Enter>", button.on_enter)
            button.bind("<Leave>", button.on_leave)

        # Configure rows and columns
        for i in range(9):
            self.grid_rowconfigure(i, weight=1)
        for i in range(4):
            self.grid_columnconfigure(i, weight=1)

    def on_button_click(self, button_text):
        current_text = self.result_var.get()
        if button_text == '=':
            try:
                current_text = self.process_special_functions(current_text)
                result = eval(current_text, {"math": math})
                self.result_var.set(result)
            except Exception as e:
                messagebox.showerror("Error", str(e))
                self.result_var.set("")
        elif button_text in ('sqrt', '^2', 'exp', '!', 'sin', 'cos', 'tan', 'deg', 'rad', 'asin', 'acos', 'atan', 'abs', 'sinh', 'cosh', 'tanh'):
            self.result_var.set(current_text + button_text)
        else:
            self.result_var.set(current_text + button_text)

    def process_special_functions(self, text):
        if 'sqrt' in text:
            text = text.replace('sqrt', 'math.sqrt')
        if '^2' in text:
            text = text.replace('^2', '**2')
        if 'exp' in text:
            text = text.replace('exp', 'math.exp')
        if '!' in text:
            text = text.replace('!', 'math.factorial')
        if 'sin' in text:
            text = text.replace('sin', 'math.sin(math.radians')
        if 'cos' in text:
            text = text.replace('cos', 'math.cos(math.radians')
        if 'tan' in text:
            text = text.replace('tan', 'math.tan(math.radians')
        if 'deg' in text:
            text = text.replace('deg', '*math.pi/180')
        if 'rad' in text:
            text = text.replace('rad', '*180/math.pi')
        if 'asin' in text:
            text = text.replace('asin', 'math.degrees(math.asin')
        if 'acos' in text:
            text = text.replace('acos', 'math.degrees(math.acos')
        if 'atan' in text:
            text = text.replace('atan', 'math.degrees(math.atan')
        if 'abs' in text:
            text = text.replace('abs', 'math.fabs')
        if 'sinh' in text:
            text = text.replace('sinh', 'math.sinh')
        if 'cosh' in text:
            text = text.replace('cosh', 'math.cosh')
        if 'tanh' in text:
            text = text.replace('tanh', 'math.tanh')
        return text

class CalculatorApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Advanced Calculator")
        self.geometry("800x800")
        self.configure(bg='#ECEFF1')

        self.create_widgets()

    def create_widgets(self):
        # Create hamburger menu frame
        self.menu_frame = tk.Frame(self, bg='#CFD8DC', width=100)
        self.menu_frame.pack(side=tk.LEFT, fill=tk.Y)
        
        # Create the toggle button
        self.toggle_button = tk.Button(self.menu_frame, text="☰", font=("Arial", 24), command=self.toggle_menu, bg='#B0BEC5', fg='#FFFFFF', relief=tk.FLAT)
        self.toggle_button.pack(pady=10)

        # Create the container for the calculator frames
        self.container = tk.Frame(self)
        self.container.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        # Create the calculator frames
        self.financial_calculator = FinancialCalculator(self.container)
        self.scientific_calculator = ScientificCalculator(self.container)

        # Display financial calculator by default
        self.financial_calculator.grid(row=0, column=0, sticky='nsew')
        self.scientific_calculator.grid(row=0, column=0, sticky='nsew')
        self.scientific_calculator.grid_forget()  # Hide scientific calculator initially

        # Configure rows and columns
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

    def toggle_menu(self):
        if self.financial_calculator.winfo_ismapped():
            self.financial_calculator.grid_forget()
            self.scientific_calculator.grid(row=0, column=0, sticky='nsew')
        else:
            self.scientific_calculator.grid_forget()
            self.financial_calculator.grid(row=0, column=0, sticky='nsew')

if __name__ == "__main__":
    app = CalculatorApp()
    app.mainloop()
