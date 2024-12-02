from tkinter import *
from tkinter import filedialog as fd

def insert_text():
    file_name = fd.askopenfilename()
    print(file_name)
    f = open(file_name)
    s = f.read()
    #print(s)
    text.insert(1.0, s)
    numbers = []
    for i in s.split(" "):
        numbers.append(float(i))

    max_elem = numbers[0]
    sum = 0
    for num in numbers:
        if num > max_elem:
            max_elem = num
        sum += num
    print(f'Largest element: {max_elem}')
    label = Label(text = (f'The largest element: {max_elem}'))
    label.grid(row = 3, column = 3, columnspan = 3)
    print(f'Sum: {sum}')
    label = Label(text = (f'Sum: {sum}'))
    label.grid(row = 4, column = 3, columnspan = 3)
root = Tk()
#root.geometry('500x500')
label = Label(text = 'The contents of the file: ')
label.grid(row = 0, column = 0, columnspan = 2)

text = Text(root, width = 40, height = 4, wrap = WORD, font='Verdana 30')
text.grid(row=0, column=2, columnspan=10)

btn = Button(text = 'Open', command = insert_text)
btn.grid(row = 2, column = 0, pady = 10)
root.mainloop()