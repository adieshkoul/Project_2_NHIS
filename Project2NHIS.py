
import tkinter as tk
import math

# ---------------- Main Window ----------------
root = tk.Tk()
root.title("Advanced Calculator")
root.geometry("360x540")
root.resizable(False, False)

# ---------------- Display ----------------
display = tk.Entry(
    root,
    font=("Arial", 24),
    borderwidth=10,
    relief="ridge",
    justify="right"
)
display.pack(fill="both", padx=10, pady=10, ipady=10)

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
        display.delete(0, tk.END)
        display.insert(0, "Error")

def cube():
    try:
        value = float(display.get())
        display.delete(0, tk.END)
        display.insert(0, value ** 3)
    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")

def square_root():
    try:
        value = float(display.get())
        display.delete(0, tk.END)
        display.insert(0, math.sqrt(value))
    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")

def reciprocal():
    try:
        value = float(display.get())
        display.delete(0, tk.END)
        display.insert(0, 1 / value)
    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")

# ---------------- BUTTONS ----------------
buttons = [
    ("C", clear_display), ("⌫", backspace), ("%", lambda: insert_value("%")), ("/", lambda: insert_value("/")),
    ("7", lambda: insert_value("7")), ("8", lambda: insert_value("8")), ("9", lambda: insert_value("9")), ("*", lambda: insert_value("*")),
    ("4", lambda: insert_value("4")), ("5", lambda: insert_value("5")), ("6", lambda: insert_value("6")), ("-", lambda: insert_value("-")),
    ("1", lambda: insert_value("1")), ("2", lambda: insert_value("2")), ("3", lambda: insert_value("3")), ("+", lambda: insert_value("+")),
    (".", lambda: insert_value(".")), ("0", lambda: insert_value("0")), ("x²", square), ("x³", cube),
    ("√", square_root), ("1/2", reciprocal), ("=", calculate)
]

# ---------------- LAYOUT ----------------
frame = tk.Frame(root)
frame.pack(expand=True, fill="both")

row = 0
col = 0

for (text, command) in buttons:
    btn = tk.Button(
        frame,
        text=text,
        command=command,
        font=("Arial", 16),
        height=2,
        width=5
    )
    btn.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
    col += 1
    if col > 3:
        col = 0
        row += 1

# Responsive grid
for i in range(6):
    frame.rowconfigure(i, weight=1)
for j in range(4):
    frame.columnconfigure(j, weight=1)

# ---------------- Run App ----------------
root.mainloop()
