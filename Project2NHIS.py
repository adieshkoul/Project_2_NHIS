
import tkinter as tk
import math

# ---------------- Main Window ----------------
root = tk.Tk()
root.title("Advanced Calculator")
root.geometry("380x560")
root.resizable(False, False)
root.configure(bg="#1e1e1e")  # Dark background

# ---------------- Display ----------------
display = tk.Entry(
    root,
    font=("Arial", 26),
    bg="#2d2d2d",
    fg="white",
    insertbackground="white",
    borderwidth=8,
    relief="ridge",
    justify="right"
)
display.pack(fill="both", padx=15, pady=15, ipady=12)

# ---------------- Functions ----------------
def insert_value(value):
    display.insert(tk.END, value)

def clear_display():
    display.delete(0, tk.END)

def backspace():
    current = display.get()
    display.delete(0, tk.END)
    display.insert(0, current[:-1])

def calculate():
    try:
        result = eval(display.get())
        display.delete(0, tk.END)
        display.insert(0, str(result))
    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")

def square():
    try:
        value = float(display.get())
        display.delete(0, tk.END)
        display.insert(0, value ** 2)
    except:
        display.insert(0, "Error")

def cube():
    try:
        value = float(display.get())
        display.delete(0, tk.END)
        display.insert(0, value ** 3)
    except:
        display.insert(0, "Error")

def square_root():
    try:
        value = float(display.get())
        display.delete(0, tk.END)
        display.insert(0, math.sqrt(value))
    except:
        display.insert(0, "Error")

def reciprocal():
    try:
        value = float(display.get())
        display.delete(0, tk.END)
        display.insert(0, 1 / value)
    except:
        display.insert(0, "Error")

# ---------------- Button Styling ----------------
button_bg = "#3c3f41"
button_fg = "white"
operator_bg = "#ff9500"
special_bg = "#d32f2f"

# ---------------- Buttons ----------------
buttons = [
    ("C", clear_display, special_bg),
    ("⌫", backspace, special_bg),
    ("%", lambda: insert_value("%"), operator_bg),
    ("/", lambda: insert_value("/"), operator_bg),

    ("7", lambda: insert_value("7"), button_bg),
    ("8", lambda: insert_value("8"), button_bg),
    ("9", lambda: insert_value("9"), button_bg),
    ("*", lambda: insert_value("*"), operator_bg),

    ("4", lambda: insert_value("4"), button_bg),
    ("5", lambda: insert_value("5"), button_bg),
    ("6", lambda: insert_value("6"), button_bg),
    ("-", lambda: insert_value("-"), operator_bg),

    ("1", lambda: insert_value("1"), button_bg),
    ("2", lambda: insert_value("2"), button_bg),
    ("3", lambda: insert_value("3"), button_bg),
    ("+", lambda: insert_value("+"), operator_bg),

    (".", lambda: insert_value("."), button_bg),
    ("0", lambda: insert_value("0"), button_bg),
    ("00", lambda: insert_value("00"), button_bg),
    ("√", square_root, operator_bg),
    
    ("x²", square, operator_bg),
    ("x³", cube, operator_bg),
    ("1/x", reciprocal, operator_bg),
    ("=", calculate, "#4CAF50"),
]

# ---------------- Layout ----------------
frame = tk.Frame(root, bg="#1e1e1e")
frame.pack(expand=True, fill="both")

row = 0
col = 0

for (text, command, color) in buttons:
    btn = tk.Button(
        frame,
        text=text,
        command=command,
        font=("Arial", 16, "bold"),
        bg=color,
        fg=button_fg,
        activebackground="#616161",
        activeforeground="white",
        relief="flat",
        height=2,
        width=5
    )
    btn.grid(row=row, column=col, padx=6, pady=6, sticky="nsew")
    col += 1
    if col > 3:
        col = 0
        row += 1

for i in range(6):
    frame.rowconfigure(i, weight=1)
for j in range(4):
    frame.columnconfigure(j, weight=1)

root.mainloop()