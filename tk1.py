import tkinter as tk

def calculate_subtraction():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result = num1 - num2
        result_label.config(text=f"Result: {result}")
    except ValueError:
        result_label.config(text="Invalid input")

# Create the main window
root = tk.Tk()
root.title("Number Subtraction Tool")

# Create input boxes
entry1 = tk.Entry(root)
entry2 = tk.Entry(root)

# Create Calculate button
calculate_button = tk.Button(root, text="Calculate", command=calculate_subtraction)

# Create result label
result_label = tk.Label(root, text="Result: ")

# Place widgets using grid layout
entry1.grid(row=0, column=0, padx=10, pady=10)
entry2.grid(row=0, column=1, padx=10, pady=10)
calculate_button.grid(row=1, columnspan=2, padx=10, pady=10)
result_label.grid(row=2, columnspan=2, padx=10, pady=10)

# Start the GUI event loop
root.mainloop()
