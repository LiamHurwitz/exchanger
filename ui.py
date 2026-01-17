import tkinter as tk
import tkinter.messagebox as messagebox

from yendata import *
# Run useful functions from yendata before main loop
initialRequest()
conversion_rate = currencyParse()

root = tk.Tk()
root.title("Convertinator 9000")
root.geometry("600x400")

"""
GUI Layout:
    Label: USD to Yen
    Text Box parsing for integer
    Button: Convert
    Output box 

    Label: Yen to USD
    Text box parsing for integer
    Button: Convert
    Output box
"""

tk.Label(root, text="USD to Yen (Enter USD): ").pack()
dollar_entry = tk.Entry(root)
dollar_entry.pack()

tk.Label(root, text="Yen to USD (Enter Yen): ").pack()
yen_entry = tk.Entry(root)
yen_entry.pack()

def convertDtoY():
    dollar_value = float(dollar_entry.get())
    yen_conv_value = dollar_value * conversion_rate

    tk.messagebox.showinfo("Results", f"That's worth {yen_conv_value} Yen!")

def convertYtoD():
    yen_value = float(yen_entry.get())
    dollar_conv_value = yen_value / conversion_rate

    tk.messagebox.showinfo("Results", f"That's worth {dollar_conv_value} Dollars!")

tk.Button(root, text="Convert USD -> Yen",
          command=convertDtoY).pack(pady=10)

tk.Button(root, text="Convert Yen -> USD",
          command=convertYtoD).pack(pady=10)

root.mainloop()













