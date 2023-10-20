import tkinter as tk

def calculate():
    try:
        expression = entry.get()
        result = eval(expression)
        decimal_result.set(f"Decimal: {result}")
        binary_result.set(f"Binary: {bin(int(result))}")
        hexadecimal_result.set(f"Hexadecimal: {hex(int(result))}")
        octal_result.set(f"Octal: {oct(int(result))}")
    except Exception as e:
        decimal_result.set("Error")
        binary_result.set("Error")
        hexadecimal_result.set("Error")
        octal_result.set("Error")

# Create the main window
root = tk.Tk()
root.title("Unique Calculator")

# Entry field for input
entry = tk.Entry(root, width=30)
entry.grid(row=0, column=0, columnspan=4)

# Buttons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row_val = 1
col_val = 0

for button in buttons:
    if button == '=':
        tk.Button(root, text=button, padx=20, pady=20, command=calculate).grid(row=row_val, column=col_val)
    else:
        tk.Button(root, text=button, padx=20, pady=20, command=lambda button=button: entry.insert(tk.END, button)).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Result labels
decimal_result = tk.StringVar()
binary_result = tk.StringVar()
hexadecimal_result = tk.StringVar()
octal_result = tk.StringVar()

tk.Label(root, textvariable=decimal_result).grid(row=row_val, column=0, columnspan=4)
row_val += 1
tk.Label(root, textvariable=binary_result).grid(row=row_val, column=0, columnspan=4)
row_val += 1
tk.Label(root, textvariable=hexadecimal_result).grid(row=row_val, column=0, columnspan=4)
row_val += 1
tk.Label(root, textvariable=octal_result).grid(row=row_val, column=0, columnspan=4)

root.mainloop()
