import tkinter as tk
from tkinter import messagebox

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("CALCULATOR")
        master.geometry("300x400")
        master.config(bg='#2C3E50')
        
        self.result_var = tk.StringVar()
        self.result_var.set("0")
        
        self.display = tk.Entry(master, textvariable=self.result_var, justify="right",
                                font=("Arial", 24), bg="#ECF0F1", fg="#2C3E50")
        self.display.grid(row=0, column=0, columnspan=4, padx=5, pady=5)
        
        buttons = [('7','#3498DB'), ('8','#3498DB'),('9','#3498DB'),('/','#E74C3C'),
                   ('4','#3498DB'), ('5','#3498DB'), ('6','#3498DB'), ('*','#E74C3C'),
                   ('1','#3498DB'), ('2','#3498DB'), ('3','#3498DB'),('-','#E74C3C'),
                   ('0','#3498DB'), ('.','#3498DB'), ('C','#E67E22'),('+','#E74C3C')]
        
        row = 1
        col = 0
        
        for (button, color) in buttons:
            cmd = lambda x=button: self.click(x)
            tk.Button(master, text=button, command=cmd, width=5, height=2,
                      font=("Arial",14), bg=color, fg='white', activebackground='#85929E').grid(row=row, column=col, padx=2, pady=2)
            
            col += 1
            if col > 3:
                col = 0
                row += 1
                
        tk.Button(master, text='=', command=self.calculate, width=5, height=2,
                  font=("Arial", 14), bg='#27AE60', fg='white', 
                  activebackground='#85929E').grid(row=row, column=col, padx=2, pady=2)
    
    def click(self, key):
        if key == 'C':
            self.result_var.set("0")
        else:
            if self.result_var.get() == "0":
                self.result_var.set(key)
            else:
                self.result_var.set(self.result_var.get() + key)
    
    def calculate(self):
        try:
            result = eval(self.result_var.get())
            self.result_var.set(result)
        except Exception as e:
            messagebox.showerror("Error", f"Invalid input: {str(e)}")
            self.result_var.set("0")

root = tk.Tk()
calculator = Calculator(root)
root.mainloop()