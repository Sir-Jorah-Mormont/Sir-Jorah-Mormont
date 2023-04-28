import tkinter as tk

class BondCalculator:
    def __init__(self, symbol1, symbol2):
        self.symbol1 = symbol1
        self.symbol2 = symbol2

    def calculate_bond_type(self):
        electronegativity = {"H": 2.20, "Li": 0.98, "Be": 1.57, "B": 2.04, "C": 2.55,
                             "N": 3.04, "O": 3.44, "F": 3.98, "Na": 0.93, "Mg": 1.31,
                             "Al": 1.61, "Si": 1.90, "P": 2.19, "S": 2.58, "Cl": 3.16,
                             "K": 0.82, "Ca": 1.00, "Fe": 1.83, "Cu": 1.90, "Zn": 1.65}

        elec1 = electronegativity.get(self.symbol1)
        elec2 = electronegativity.get(self.symbol2)

        if elec1 is None or elec2 is None:
            return "Invalid symbol(s) entered."

        delta_e = abs(elec1 - elec2)

        if delta_e < 1.7:
            return "The bond between {} and {} is covalent.".format(self.symbol1, self.symbol2)
        else:
            return "The bond between {} and {} is ionic.".format(self.symbol1, self.symbol2)

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        self.title_label = tk.Label(self.master, text="Bond Calculator")
        self.title_label.pack()

        self.symbol1_label = tk.Label(self.master, text="Enter the first chemical symbol:")
        self.symbol1_label.pack()

        self.symbol1_entry = tk.Entry(self.master)
        self.symbol1_entry.pack()

        self.symbol2_label = tk.Label(self.master, text="Enter the second chemical symbol:")
        self.symbol2_label.pack()

        self.symbol2_entry = tk.Entry(self.master)
        self.symbol2_entry.pack()

        self.calculate_button = tk.Button(self.master, text="Calculate", command=self.calculate_bond)
        self.calculate_button.pack()

        self.reset_button = tk.Button(self.master, text="Reset", command=self.reset_fields)
        self.reset_button.pack()

        self.result_label = tk.Label(self.master, text="")
        self.result_label.pack()

    def calculate_bond(self):
        symbol1 = self.symbol1_entry.get()
        symbol2 = self.symbol2_entry.get()

        calculator = BondCalculator(symbol1, symbol2)
        result = calculator.calculate_bond_type()

        self.result_label.config(text=result)

    def reset_fields(self):
        self.symbol1_entry.delete(0, tk.END)
        self.symbol2_entry.delete(0, tk.END)
        self.result_label.config(text="")

root = tk.Tk()
app = Application(master=root)
app.mainloop()
