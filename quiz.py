import tkinter as tk
from tkinter import ttk

def calculate_score():
    score = 0

    if entry_answer.get().lower() == "python":
        score += 1

    if listbox_answer.get(tk.ACTIVE) == "Green":
        score += 1

    if combobox_answer.get() == "Dog":
        score += 1

    if radio_var.get() == 3:
        score += 1

    if check_var1.get() == 1 and check_var2.get() == 1 and check_var3.get() == 0 and check_var4.get() == 0:
        score += 1

    result_label.config(text=f"You have scored {score} out of 5 points")

root = tk.Tk()
root.title("Quiz")

tk.Label(root, text="1. What programming language is used in this code?").pack()
entry_answer = tk.Entry(root)
entry_answer.pack()

tk.Label(root, text="2. My favourite colour: ").pack()
listbox_answer = tk.Listbox(root)
listbox_answer.insert(1, "Red")
listbox_answer.insert(2, "Green")
listbox_answer.insert(3, "Blue")
listbox_answer.pack()

tk.Label(root, text="3. My favourite pet: ").pack()
combobox_answer = ttk.Combobox(root, values=["Cat", "Dog", "Parrot"])
combobox_answer.pack()

tk.Label(root, text="4. What number can be divided by 0?").pack()
radio_var = tk.IntVar()
tk.Radiobutton(root, text="515", variable=radio_var, value=1).pack()
tk.Radiobutton(root, text="0", variable=radio_var, value=2).pack()
tk.Radiobutton(root, text="You can't divide by 0", variable=radio_var, value=3).pack()

tk.Label(root, text="5. Pick 2 correct answers: ").pack()
check_var1 = tk.IntVar()
check_var2 = tk.IntVar()
check_var3 = tk.IntVar()
check_var4 = tk.IntVar()

tk.Checkbutton(root, text="The Earth is round", variable=check_var1).pack()
tk.Checkbutton(root, text="The water is wet", variable=check_var2).pack()
tk.Checkbutton(root, text="The sun is cold", variable=check_var3).pack()
tk.Checkbutton(root, text="The moon is made of cheese", variable=check_var4).pack()

submit_button = tk.Button(root, text="Send reply", command=calculate_score)
submit_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()

