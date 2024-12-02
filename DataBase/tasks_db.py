import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import sqlite3


conn = sqlite3.connect("to_do_list.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT NOT NULL,
    completed BOOLEAN NOT NULL CHECK(completed IN(0, 1))
)
""")

conn.commit()

def add_task():
    title = entry_title.get()
    description = entry_descr.get()
    if title and description:
        cursor.execute(
            'INSERT INTO tasks (title, description, completed) VALUES (?, ?, 0)', (title, description))
        conn.commit()
        entry_descr.delete(0, tk.END)
        entry_title.delete(0, tk.END)
        show_tasks()
    else:
        messagebox.showwarning('ошибка', 'поля не должны быть пустыми')


def show_tasks():
    for item in tree.get_children():
        tree.delete(item)
    cursor.execute('SELECT * FROM tasks')
    tasks = cursor.fetchall()
    for task in tasks:
        print(task)
        #status = 'Выполнено' if task[3] else 'Невыполнено'
        tags = ('completed',) if task[3] else ('pending',)
        status = ''
        if task[3] == 1:
            status = 'Выполнено'
        else:
            status = 'Невыполнено'
        tree.insert('', tk.END, values=(task[0], task[1], task[2], status), tags = tags)

def delete_task():
    selected_item = tree.selection()
    if selected_item:
        task_id = tree.item(selected_item)['values'][0]
        print(task_id)
        cursor.execute('DELETE FROM tasks WHERE id = ?', (task_id, ))
        conn.commit()
        show_tasks()
    else:
        messagebox.showwarning('Ошибка', 'Выберите задачу')

def complete_task():
    selected_item = tree.selection()
    if selected_item:
        task_id = tree.item(selected_item)['values'][0]
        print(task_id)
        cursor.execute('UPDATE tasks SET completed = 1 WHERE id = ?', (task_id, ))
        conn.commit()
        show_tasks()
        
    else:
        messagebox.showwarning('Ошибка', 'Выберите задачу')
def uncomplete_task():
    selected_item = tree.selection()
    if selected_item:
        task_id = tree.item(selected_item)['values'][0]
        print(task_id)
        cursor.execute('UPDATE tasks SET completed = 0 WHERE id = ?', (task_id, ))
        conn.commit()
        show_tasks()
        
    else:
        messagebox.showwarning('Ошибка', 'Выберите задачу')




root = tk.Tk()
root.title('tasks app')

frame_title = tk.Frame(root)
frame_title.pack(pady=10)

tk.Label(frame_title, text = 'Заголовок:').pack(side = tk.LEFT, padx=10)
entry_title = tk.Entry(frame_title, width = 50)
entry_title.pack(side = tk.LEFT, padx=10)



frame_descr = tk.Frame(root)
frame_descr.pack(pady=10)

tk.Label(frame_descr, text = 'Описание задачи:').pack(side = tk.LEFT, padx=10)
entry_descr = tk.Entry(frame_descr, width = 50)
entry_descr.pack(side = tk.LEFT, padx=10)


button = tk.Button(root, text='Добавить задачу', command=add_task)
button.pack()


columns = ("ID", "Заголовок", "Текст", "Статус")
tree = ttk.Treeview(root, columns=columns, show='headings')
tree.heading("ID", text="ID")
tree.heading("Заголовок", text="Заголовок")
tree.heading("Текст", text="Текст")
tree.heading("Статус", text="Статус")

tree.column('ID', width=50, anchor=tk.CENTER)
tree.column('Заголовок', width=200, anchor=tk.CENTER)
tree.column('Текст', width=250, anchor=tk.CENTER)
tree.column('Статус', width=100, anchor=tk.CENTER)
tree.pack()

style = ttk.Style()
style.configure("Treeview", font=('Arial', 12))
style.configure('Treeview.Heading', font=('Arial', 14, 'bold'))
style.map('Treeview', background=[('selected', '#ccc')])
tree.tag_configure('completed', background='light green')
tree.tag_configure('pending', background='orange')

frame_buttons = tk.Frame(root)
frame_buttons.pack(pady=10)

delete_button = tk.Button(frame_buttons, text='Удалить задачу', command=delete_task)
delete_button.pack(side=tk.LEFT, padx=10)

complete_task = tk.Button(frame_buttons, text='Выполнить задачу', command=complete_task)
complete_task.pack(side=tk.RIGHT)

complete_task = tk.Button(frame_buttons, text='Отменить выполненую задачу', command=uncomplete_task)
complete_task.pack(side=tk.RIGHT, padx=10)

show_tasks()

root.mainloop()