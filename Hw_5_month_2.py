""" Домашнее задание """

" 1 "

import sqlite3

conn = sqlite3.connect("School.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        full_name TEXT NOT NULL,
        age INTEGER,
        grade TEXT NOT NULL,
        enrollment_date DATE 
    )
""")

conn.commit()



cursor.execute("""
    CREATE TABLE IF NOT EXISTS subjects (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        subject_name TEXT NOT NULL,
        teacher_name TEXT NOT NULL
    )
""")

conn.commit()




" 2 "

def register_student():
    full_name = input("Введите полное имя: ")
    age = int(input("Укажите возраст: "))
    grade = input("Укажите класс: ")
    enrollment_date =  input("Укажите сегодняшнюю дату: ")
    
    cursor.execute('''
        INSERT INTO students (full_name, age, grade, enrollment_date)
        VALUES (?, ?, ?, ?)
    ''', (full_name, age, grade, enrollment_date))
    
    conn.commit()
    print("Студент успешно добавлен.")

# register_student()
    



def add_subjects():
    subject_name = input("Введите название предмета: ")
    teacher_name = input("Введите имя учителя: ")
    
    cursor.execute("""
        INSERT INTO subjects (subject_name, teacher_name)
        VALUES (?, ?)   
    """, (subject_name, teacher_name))
    
    conn.commit()
    print("Предмет успешно добавлен.")
    

# add_subjects()
    


 
 
" 3 " 
   
def get_students():
    cursor.execute("""SELECT * FROM students""")
    students = cursor.fetchall()
    print(students)
    
    conn.commit()

# get_students()
        

def get_subject():
    cursor.execute("""SELECT * FROM subjects""")
    subjects = cursor.fetchall()
    
    print(subjects)
    conn.commit()
    
# get_subject()
        
 

def get_students_by_grade(grade):
    cursor.execute("""SELECT * FROM students WHERE grade = ?""", (grade,))
    students = cursor.fetchall()

    print(students)
 
# get_students_by_grade(2)
 
 
 
       
" 4 "

def update_student_age(student_id, new_age):
    cursor.execute("""
        UPDATE students
        SET age = ?
        WHERE id = ?
    """, (new_age, student_id))
    
    conn.commit()
    print(f"Возраст студента с ID {student_id} обновлен до {new_age}.")
    
# update_student_age(1,20)


def delete_student(student_id):
    cursor.execute("""
        DELETE FROM students
        WHERE id = ?
    """, (student_id,))
    
    conn.commit()
    print(f"Студент с ID {student_id} был удален.")
    
# delete_student(3)