import tkinter as tk
from tkinter import ttk

def roman_to_decimal(roman):
    roman_numerals = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
    }

    decimal = 0
    prev_value = 0

    for numeral in reversed(roman):
        value = roman_numerals.get(numeral, 0)

        if value < prev_value:
            decimal -= value
        else:
            decimal += value

        prev_value = value

    return decimal

def convert():
    roman_numeral = roman_entry.get().upper()
    decimal_number = roman_to_decimal(roman_numeral)
    result_label.config(text=f"Decimal equivalent: {decimal_number}")

# Create the main window
root = tk.Tk()
root.title("Roman to Decimal Converter")

# Create and place widgets
style = ttk.Style()
style.configure("TLabel", font=("Helvetica", 14))
style.configure("TButton", font=("Helvetica", 14))
style.configure("TButton", borderwidth=10)

frame = ttk.Frame(root, padding=10)
frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

roman_label = ttk.Label(frame, text="Enter a Roman numeral:")
roman_label.grid(column=0, row=0, sticky=tk.W, padx=10, pady=10)

roman_entry = ttk.Entry(frame, font=("Helvetica", 14))
roman_entry.grid(column=0, row=1, columnspan=2, sticky=(tk.W, tk.E), padx=10, pady=10)

convert_button = ttk.Button(frame, text="Convert", command=convert, style="TButton")
convert_button.grid(column=0, row=2, columnspan=2, sticky="nsew", padx=10, pady=20)

result_label = ttk.Label(frame, text="", font=("Helvetica", 16, "bold"))
result_label.grid(column=0, row=3, columnspan=2, sticky=(tk.W, tk.E), padx=10, pady=10)

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# Start the main loop
root.mainloop()
