import sqlite3


def create_database():
    with sqlite3.connect("../school.db") as connection:
        connection.execute("""
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                age INTEGER,
                grade REAL
            )
        """)


def add_student(name, age, grade):
    with sqlite3.connect("../school.db") as connection:
        connection.execute(
            "INSERT INTO students (name, age, grade) VALUES (?, ?, ?)",
            (name, age, grade)
        )


def show_students():
    with sqlite3.connect("../school.db") as connection:
        cursor = connection.execute(
            "SELECT id, name, age, grade FROM students ORDER BY id"
        )

        for student in cursor.fetchall():
            print(student)


def show_average_grade():
    with sqlite3.connect("../school.db") as connection:
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


# as class (oop)
# import sqlite3
#
#
# class StudentManager:
#
#     def __init__(self, database="students.db"):
#         self.connection = sqlite3.connect(database)
#
#         self.connection.execute("""
#             CREATE TABLE IF NOT EXISTS students (
#                 id INTEGER PRIMARY KEY AUTOINCREMENT,
#                 name TEXT NOT NULL,
#                 age INTEGER,
#                 grade REAL
#             )
#         """)
#
#         self.connection.commit()
#
#     def add_student(self, name, age, grade):
#         self.connection.execute(
#             """
#             INSERT INTO students (name, age, grade)
#             VALUES (?, ?, ?)
#             """,
#             (name, age, grade)
#         )
#
#         self.connection.commit()
#         print("Student added successfully.")
#
#     def show_students(self):
#         rows = self.connection.execute(
#             "SELECT * FROM students ORDER BY id"
#         ).fetchall()
#
#         for row in rows:
#             print(row)
#
#     def find_student(self, student_id):
#         row = self.connection.execute(
#             "SELECT * FROM students WHERE id = ?",
#             (student_id,)
#         ).fetchone()
#
#         if row:
#             print(row)
#         else:
#             print("Student not found.")
#
#     def update_grade(self, student_id, new_grade):
#         cursor = self.connection.execute(
#             "UPDATE students SET grade = ? WHERE id = ?",
#             (new_grade, student_id)
#         )
#
#         self.connection.commit()
#
#         if cursor.rowcount > 0:
#             print("Grade updated successfully.")
#         else:
#             print("Student not found.")
#
#     def delete_student(self, student_id):
#         cursor = self.connection.execute(
#             "DELETE FROM students WHERE id = ?",
#             (student_id,)
#         )
#
#         self.connection.commit()
#
#         if cursor.rowcount > 0:
#             print("Student deleted successfully.")
#         else:
#             print("Student not found.")
#
#     def close(self):
#         self.connection.close()



# manager = StudentManager()
#
# manager.add_student("Ali", 18, 19.5)
# manager.add_student("Sara", 17, 18.75)
# manager.add_student("Reza", 19, 16.0)
#
# print("\nAll students:")
# manager.show_students()
#
# print("\nFind student:")
# manager.find_student(1)
#
# print("\nUpdate grade:")
# manager.update_grade(1, 20)
#
# print("\nDelete student:")
# manager.delete_student(2)
#
# print("\nFinal list:")
# manager.show_students()
#
# manager.close()