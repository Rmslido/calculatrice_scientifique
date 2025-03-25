# Intéressé par une collaboration ? Contactez-moi :
# Facebook: Rms lido
# WhatsApp: +261 34 59 743 21
# Portfolio: (https://elido-ramiandrisoa.vercel.app)

import tkinter as tk
import math

class CalculatriceScientifique:
    def __init__(self, master):
        self.master = master
        self.master.title("Calculatrice Scientifique")
        self.master.geometry("400x500")
        self.master.resizable(False, False)
        self.master.configure(bg="#f0f0f0")

        self.expression = ""
        
        self.display = tk.Entry(master, font=("Arial", 20), bd=10, insertwidth=1, width=20,
                               justify="right", bg="#e8e8e8")
        self.display.grid(row=0, column=0, columnspan=5, padx=10, pady=10)
        
        self.create_buttons()
        
    def create_buttons(self):
        buttons = [
            ('sin', 1, 0), ('cos', 1, 1), ('tan', 1, 2), ('(', 1, 3), (')', 1, 4),
            ('log', 2, 0), ('ln', 2, 1), ('√', 2, 2), ('^', 2, 3), ('π', 2, 4),
            ('7', 3, 0), ('8', 3, 1), ('9', 3, 2), ('/', 3, 3), ('C', 3, 4),
            ('4', 4, 0), ('5', 4, 1), ('6', 4, 2), ('*', 4, 3), ('AC', 4, 4),
            ('1', 5, 0), ('2', 5, 1), ('3', 5, 2), ('-', 5, 3), ('e', 5, 4),
            ('0', 6, 0), ('.', 6, 1), ('%', 6, 2), ('+', 6, 3), ('=', 6, 4),
        ]
        
        button_colors = {
            'digits': "#ffffff",
            'operators': "#e1e1e1",
            'functions': "#d1d1d1",
            'equals': "#ff9980",
            'clear': "#ffcc80"
        }
        
        for (text, row, col) in buttons:
            if text.isdigit() or text == '.':
                color = button_colors['digits']
            elif text in ['+', '-', '*', '/', '^', '%']:
                color = button_colors['operators']
            elif text in ['sin', 'cos', 'tan', 'log', 'ln', '√', 'π', 'e']:
                color = button_colors['functions']
            elif text in ['C', 'AC']:
                color = button_colors['clear']
            elif text == '=':
                color = button_colors['equals']
            else:
                color = button_colors['operators']
            
            button = tk.Button(self.master, text=text, font=("Arial", 12), 
                              width=5, height=2, bg=color,
                              command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col, padx=2, pady=2)
    
    def on_button_click(self, value):
        if value == '=':
            try:
                expr = self.expression.replace('sin', 'math.sin')
                expr = expr.replace('cos', 'math.cos')
                expr = expr.replace('tan', 'math.tan')
                expr = expr.replace('log', 'math.log10')
                expr = expr.replace('ln', 'math.log')
                expr = expr.replace('√', 'math.sqrt')
                expr = expr.replace('^', '**')
                expr = expr.replace('π', 'math.pi')
                expr = expr.replace('e', 'math.e')
                
                result = eval(expr)
                self.display.delete(0, tk.END)
                self.display.insert(0, str(result))
                self.expression = str(result)
            except Exception as e:
                self.display.delete(0, tk.END)
                self.display.insert(0, "Erreur")
                self.expression = ""
        
        elif value == 'C':
            self.expression = self.expression[:-1]
            self.display.delete(0, tk.END)
            self.display.insert(0, self.expression)
        
        elif value == 'AC':
            self.expression = ""
            self.display.delete(0, tk.END)
        
        else:
            self.expression += value
            self.display.delete(0, tk.END)
            self.display.insert(0, self.expression)

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatriceScientifique(root)
    root.mainloop()
