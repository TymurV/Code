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
    choice = int(input('1 - Add new user\n2 - See all users\n3 - Find information about user by name\nYour choice: '))
    if choice == 1:
        name1 = input('Enter a name for the new user: ')
        age1 = input('Enter the age for the new user: ')
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
        print('Available names at this time: ')
        for i in range (len(rows)):
            print(rows[i][1])
        choice_name = input('Enter the name for which you want to find information: ')
        cursor.execute('SELECT * FROM users WHERE name = ?', (choice_name,))
        for i in range (len(rows)):
            if rows[i][1] == choice_name:
                print(rows[i])
conn.close()