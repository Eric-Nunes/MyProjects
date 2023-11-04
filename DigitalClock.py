import tkinter as tk
from time import strftime

def time():
    string = strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)

root = tk.Tk()
root.title("Digital Clock")

label = tk.Label(root, font=("Helvetica", 48, "bold"), background="black", foreground="lightblue")
label.pack(anchor="center")

time()

root.mainloop()
