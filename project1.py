import tkinter as tk

def on_button_click(button_text):
    if button_text == "=":
        try:
            result = eval(display_var.get())
            display_var.set(str(result))
        except Exception as e:
            display_var.set("Error")
    elif button_text == "C":
        display_var.set("")
    else:
        display_var.set(display_var.get() + button_text)

root = tk.Tk()
root.title("Interactive Calculator")
root.geometry("400x500")

display_var = tk.StringVar()
display_var.set("")

display = tk.Entry(root, textvariable=display_var, font=("Arial", 20), justify="right")
display.grid(row=0, column=0, columnspan=4)

buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+",
    "C"
]

row, col = 1, 0
for button_text in buttons:
    button = tk.Button(root, text=button_text, font=("Arial", 20), padx=20, pady=20,
                       command=lambda text=button_text: on_button_click(text))
    button.grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1

root.mainloop()
