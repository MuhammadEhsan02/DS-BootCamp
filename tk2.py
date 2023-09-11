import tkinter as tk
from tkinter import messagebox

def show_details():
    name = name_entry.get()
    age = age_entry.get()
    address = address_text.get("1.0", "end-1c")
    answer = answer_var.get()

    details_label.config(text=f"Thank you for sharing!\n\nName: {name}\nAge: {age}\nAddress: {address}\nAnswer: {answer}")
    details_label.pack()

    input_frame.pack_forget()
    submit_button.pack_forget()

root = tk.Tk()
root.title("Personal Information")
root.geometry("500x400")
root.configure(bg="lightgrey")

input_frame = tk.Frame(root, bg="white")
input_frame.pack(pady=50)

name_label = tk.Label(input_frame, text="Your Name:", font=("Helvetica", 14), bg="white")
name_label.grid(row=0, column=0, padx=10, pady=5)
name_entry = tk.Entry(input_frame, font=("Helvetica", 12))
name_entry.grid(row=0, column=1, padx=10, pady=5)

age_label = tk.Label(input_frame, text="Your Age:", font=("Helvetica", 14), bg="white")
age_label.grid(row=1, column=0, padx=10, pady=5)
age_entry = tk.Entry(input_frame, font=("Helvetica", 12))
age_entry.grid(row=1, column=1, padx=10, pady=5)

address_label = tk.Label(input_frame, text="Your Address:", font=("Helvetica", 14), bg="white")
address_label.grid(row=2, column=0, padx=10, pady=5)
address_text = tk.Text(input_frame, height=5, width=30, font=("Helvetica", 12))
address_text.grid(row=2, column=1, padx=10, pady=5)

are_you_human_label = tk.Label(input_frame, text="Please confirm you're human:", font=("Helvetica", 14), bg="white")
are_you_human_label.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

answer_var = tk.StringVar()
yes_button = tk.Radiobutton(input_frame, text="Yes", variable=answer_var, value="Yes", font=("Helvetica", 12), bg="white")
yes_button.grid(row=4, column=0, padx=10, pady=5)
no_button = tk.Radiobutton(input_frame, text="No", variable=answer_var, value="No", font=("Helvetica", 12), bg="white")
no_button.grid(row=4, column=1, padx=10, pady=5)

submit_button = tk.Button(root, text="Submit", command=show_details, font=("Helvetica", 14), bg="lightgreen")
submit_button.pack(pady=(20, 0))

details_label = tk.Label(root, text="", font=("Helvetica", 14), bg="lightgray")
details_label.pack()

root.mainloop()