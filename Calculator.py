import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Responsive Calculator")

        self.expression = ""
        self.result_var = tk.StringVar()
        self.result_var.set("")

        # Result Display
        self.result_label = tk.Label(master, textvariable=self.result_var, font=("Arial", 20), anchor="e", padx=10, pady=10)
        self.result_label.grid(row=0, column=0, columnspan=4, sticky="nsew")

        # Button Grid
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        row_val = 1
        col_val = 0

        for button in buttons:
            tk.Button(master, text=button, padx=20, pady=20, font=("Arial", 15),
                      command=lambda b=button: self.button_click(b)).grid(row=row_val, column=col_val, sticky="nsew")
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

        # Clear Button
        tk.Button(master, text="C", padx=20, pady=20, font=("Arial", 15),
                  command=self.clear).grid(row=row_val, column=0, sticky="nsew")

        #Delete button
        tk.Button(master, text="Del", padx=20, pady=20, font=("Arial", 15),
                  command=self.delete).grid(row=row_val, column=1, sticky="nsew")

        # Configure row and column weights for responsiveness
        for i in range(5):  # Adjust range based on button grid rows
            master.grid_rowconfigure(i, weight=1)
        for i in range(4):  # Adjust range based on button grid columns
            master.grid_columnconfigure(i, weight=1)

    def button_click(self, char):
        if char == "=":
            try:
                result = eval(self.expression)
                self.result_var.set(str(result))
                self.expression = str(result) #update expression for chained calculations
            except (SyntaxError, ZeroDivisionError):
                self.result_var.set("Error")
                self.expression = ""
            except Exception as e: #catch other errors
                self.result_var.set("Error")
                print(f"An unexpected error occurred: {e}")
                self.expression = ""
        else:
            self.expression += char
            self.result_var.set(self.expression)

    def clear(self):
        self.expression = ""
        self.result_var.set("")

    def delete(self):
        self.expression = self.expression[:-1]
        self.result_var.set(self.expression)

def main():
    root = tk.Tk()
    Calculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()