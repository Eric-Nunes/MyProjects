import tkinter as tk

def on_button_click(event):
    text = event.widget.cget("text")

    if text == "=":
        try:
            result = str(eval(entry.get()))
            entry.delete(0, "end")
            entry.insert("end", result)
        except Exception as e:
            entry.delete(0, "end")
            entry.insert("end", "Error")

    elif text == "C":
        entry.delete(0, "end")
    elif text == "Del":
        current_text = entry.get()
        entry.delete(0, "end")
        entry.insert("end", current_text[:-1])
    else:
        entry.insert("end", text)

root = tk.Tk()
root.geometry("400x600")
root.title("Calculator")

entry = tk.Entry(root, font=("Helvetica", 16), justify="right")
entry.pack(fill="both", expand=True)

button_frame = tk.Frame(root)
button_frame.pack(fill="both", expand=True)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+',
    'C', 'Del'  # Add the "Del" (delete) button
]

row, col = 1, 0

for button_text in buttons:
    button = tk.Button(button_frame, text=button_text, font=("Helvetica", 16), width=5, height=2)
    button.grid(row=row, column=col, padx=5, pady=5)
    col += 1
    if col > 3:
        col = 0
        row += 1

    button.bind("<Button-1>", on_button_click)

root.mainloop()
