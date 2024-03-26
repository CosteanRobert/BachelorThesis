import tkinter as tk
from tkinter import messagebox
from user import User

def sign_up():
    username = entry_username.get()
    password = entry_password.get()
    message = User.sign_up(username, password)
    messagebox.showinfo("Sign Up", message)

def login():
    username = entry_username.get()
    password = entry_password.get()
    message = User.login(username, password)
    messagebox.showinfo("Login", message)

# Create the main window
window = tk.Tk()
window.title("Login")

# Create labels
label_username = tk.Label(window, text="Username:")
label_username.grid(row=0, column=0, padx=10, pady=5, sticky="e")

label_password = tk.Label(window, text="Password:")
label_password.grid(row=1, column=0, padx=10, pady=5, sticky="e")

# Create entry fields
entry_username = tk.Entry(window)
entry_username.grid(row=0, column=1, padx=10, pady=5)

entry_password = tk.Entry(window, show="*")
entry_password.grid(row=1, column=1, padx=10, pady=5)

# Create buttons
btn_signup = tk.Button(window, text="Sign Up", command=sign_up)
btn_signup.grid(row=2, column=0, columnspan=2, padx=10, pady=5, sticky="we")

btn_login = tk.Button(window, text="Login", command=login)
btn_login.grid(row=3, column=0, columnspan=2, padx=10, pady=5, sticky="we")

# Run the main event loop
window.mainloop()


