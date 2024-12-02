import sqlite3

conn = sqlite3.connect('file1234.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS users
                    (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)''')

'''cursor.execute('INSERT INTO users (name, age) VALUES (?, ?)', ('abc', 12))
cursor.execute('INSERT INTO users (name, age) VALUES (?, ?)', ('abcde', 23))
conn.commit()'''


#print(rows[1][1])


while True:
    choice = int(input('1 - Добавить нового пользователя\n2 - Посмотреть всех пользователей\n3 - найти информацию о пользователе по его имени\nВаш выбор: '))
    if choice == 1:
        name1 = input('Введите имя для нового пользователя: ')
        age1 = input('Введите возраст для нового пользователя: ')
        cursor.execute('INSERT INTO users (name, age) VALUES (?, ?)', (name1, age1))
        conn.commit()
        rows = cursor.fetchall()
    elif choice == 2:        
        cursor.execute('SELECT * FROM users')
        rows = cursor.fetchall()
        for i in range (len(rows)):
            print(rows[i])
    elif choice == 3:
        cursor.execute('SELECT * FROM users')
        rows = cursor.fetchall()
        print('Доступные имена на данный момент: ')
        for i in range (len(rows)):
            print(rows[i][1])
        choice_name = input('Введите имя по которому вы хотите найти информацию: ')
        cursor.execute('SELECT * FROM users WHERE name = ?', (choice_name,))
        for i in range (len(rows)):
            if rows[i][1] == choice_name:
                print(rows[i])
conn.close()