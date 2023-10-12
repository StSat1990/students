import sqlite3

db = sqlite3.connect('mydatabase.db')

con = db.cursor()

con.execute('CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT,'
            ' age INTEGER, grade TEXT);')

def add_student(name, age, grade):
    db = sqlite3.connect('mydatabase.db')

    con = db.cursor()

    con.execute('SELECT * FROM students WHERE name = ?', (name,))
    if con.fetchone():
        pass
    else:
        con.execute('INSERT INTO students (name, age, grade) VALUES (?, ?, ?);', (name, age, grade,))

    db.commit()

def student():
    db = sqlite3.connect('mydatabase.db')

    con = db.cursor()

    result = con.execute('SELECT * FROM students').fetchall()
    print(result)

    db.commit()


def get_student_by_name(name):
    db = sqlite3.connect('mydatabase.db')

    con = db.cursor()

    result = con.execute('SELECT * FROM students WHERE name = ?;', (name,)).fetchmany()
    if result:
        print(result)
    else:
        print('Нет такого ученика')

def update_student_grade(name, grade):
    db = sqlite3.connect('mydatabase.db')

    con = db.cursor()

    result = con.execute('SELECT * FROM students WHERE name = ?;', (name,)).fetchmany()
    if result:
        con.execute("UPDATE students SET grade = ? WHERE name= ?", (grade, name))
        print(f'Ученик {name} успешно переведен в {grade}')
    else:
        print('Нет такого ученика')

    db.commit()

def del_student(name):
    db = sqlite3.connect('mydatabase.db')

    con = db.cursor()

    result = con.execute('SELECT * FROM students WHERE name = ?;', (name,)).fetchmany()
    if result:
        con.execute('DELETE FROM students WHERE name = ?;', (name,))
        print(f'Ученик {name} успешно удален')
    else:
        print('Нет такого ученика')

    db.commit()


