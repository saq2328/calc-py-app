import tkinter as tk

def add():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    result = num1 + num2
    label_result.config(text="Result: {:.2f}".format(result))

def subtract():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    result = num1 - num2
    label_result.config(text="Result: {:.2f}".format(result))

def multiply():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    result = num1 * num2
    label_result.config(text="Result: {:.2f}".format(result))

def divide():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    if num2 == 0:
        label_result.config(text="Result: Error")
    else:
        result = num1 / num2
        label_result.config(text="Result: {:.2f}".format(result))

root = tk.Tk()

label1 = tk.Label(root, text="Enter the first number:")
label1.pack()

entry1 = tk.Entry(root)
entry1.pack()

label2 = tk.Label(root, text="Enter the second number:")
label2.pack()

entry2 = tk.Entry(root)
entry2.pack()

button_add = tk.Button(root, text="+", command=add)
button_add.pack()

button_subtract = tk.Button(root, text="-", command=subtract)
button_subtract.pack()

button_multiply = tk.Button(root, text="*", command=multiply)
button_multiply.pack()

button_divide = tk.Button(root, text="/", command=divide)
button_divide.pack()

label_result = tk.Label(root, text="Result:")
label_result.pack()

root.mainloop()