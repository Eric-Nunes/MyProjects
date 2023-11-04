import tkinter as tk

def login():
    entered_username = username_entry.get()
    entered_password = password_entry.get()

    # Replace this logic with your authentication mechanism
    if entered_username == "user" and entered_password == "1234":
        result_label.config(text="Login Successful")
    else:
        result_label.config(text="Login Failed")

# Create the main window
root = tk.Tk()
root.title("Login Screen")

# Create and place widgets
username_label = tk.Label(root, text="Username:")
username_label.pack()
username_entry = tk.Entry(root)
username_entry.pack()

password_label = tk.Label(root, text="Password:")
password_label.pack()
password_entry = tk.Entry(root, show="*")  # Passwords are obscured
password_entry.pack()

login_button = tk.Button(root, text="Login", command=login)
login_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

# Start the main loop
root.mainloop()
