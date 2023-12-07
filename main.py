import tkinter as tk

# Create a function to handle button clicks
def button_click(value):
    current = input_field.get()
    input_field.delete(0, tk.END)
    input_field.insert(0, current + str(value))

def calculate_result():
    expression = input_field.get()
    try:
        result = eval(expression)  # Use eval to perform the calculation
        display_field.delete(0, tk.END)
        display_field.insert(0, result)
    except Exception as e:
        display_field.delete(0, tk.END)
        display_field.insert(0, "Error")

# Create the main window
root = tk.Tk()
root.title("Basic Calculator")

# Create input and display fields
input_field = tk.Entry(root, width=30)
display_field = tk.Entry(root, width=30)
input_field.grid(row=0, column=0, columnspan=4)
display_field.grid(row=1, column=0, columnspan=4)

# Create number buttons
button_1 = tk.Button(root, text="1", padx=20, pady=20)
button_2 = tk.Button(root, text="2", padx=20, pady=20)
button_3 = tk.Button(root, text="3", padx=20, pady=20)
button_4 = tk.Button(root, text="4", padx=20, pady=20)
button_5 = tk.Button(root, text="5", padx=20, pady=20)
button_6 = tk.Button(root, text="6", padx=20, pady=20)
button_7 = tk.Button(root, text="7", padx=20, pady=20)
button_8 = tk.Button(root, text="8", padx=20, pady=20)
button_9 = tk.Button(root, text="9", padx=20, pady=20)
button_0 = tk.Button(root, text="0", padx=20, pady=20)

buttons = [
    [button_1, 1], [button_2, 2], [button_3, 3],
    [button_4, 4], [button_5, 5], [button_6, 6],
    [button_7, 7], [button_8, 8], [button_9, 9],
    [button_0, 0]
]

for button, value in buttons:
    button.config(command=lambda v=value: button_click(v))

# Create operator buttons
button_plus = tk.Button(root, text="+", padx=20, pady=20)
button_minus = tk.Button(root, text="-", padx=20, pady=20)
button_multiply = tk.Button(root, text="x", padx=20, pady=20)
button_divide = tk.Button(root, text="÷", padx=20, pady=20)

operators = [
    [button_plus, "+"], [button_minus, "-"],
    [button_multiply, "x"], [button_divide, "÷"]
]

for button, op in operators:
    button.config(command=lambda o=op: button_click(o))

# Create an equal button to calculate the result
equal_button = tk.Button(root, text="=", padx=20, pady=20, command=calculate_result)
equal_button.grid(row=5, column=0, columnspan=4)

# Start the tkinter main loop
root.mainloop()
