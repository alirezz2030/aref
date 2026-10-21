import sqlite3


def create_database():
    with sqlite3.connect("school.db") as connection:
        connection.execute("""
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                age INTEGER,
                grade REAL
            )
        """)


def add_student(name, age, grade):
    with sqlite3.connect("school.db") as connection:
        connection.execute(
            "INSERT INTO students (name, age, grade) VALUES (?, ?, ?)",
            (name, age, grade)
        )


def show_students():
    with sqlite3.connect("school.db") as connection:
        cursor = connection.execute(
            "SELECT id, name, age, grade FROM students ORDER BY id"
        )

        for student in cursor.fetchall():
            print(student)


def show_average_grade():
    with sqlite3.connect("school.db") as connection:
        cursor = connection.execute(
            "SELECT AVG(grade) FROM students"
        )

        average = cursor.fetchone()[0]
        print("Average grade:", average)


create_database()

add_student("Ali", 20, 18.5)
add_student("Sara", 22, 19.0)

print("All students:")
show_students()

show_average_grade()