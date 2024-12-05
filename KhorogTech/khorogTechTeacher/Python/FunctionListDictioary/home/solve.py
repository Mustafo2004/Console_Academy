# Задача 1
def add_student(students, name, grade):
    students.append({'name': name, 'grade': grade})


# Задача 3
def update_grade(students, name, new_grade):
    for student in students:
        if student['name'] == name:
            student['grade'] = new_grade
            break

# Задача 4
def get_student_grade(students, name):
    for student in students:
        if student['name'] == name:
            return student['grade']
    return None

# Задача 5
def print_students(students):
    for student in students:
        print(f"Имя: {student['name']}, Оценка: {student['grade']}")

# Задача 6
def add_subject(students, name, subject, grade):
    for student in students:
        if student['name'] == name:
            if 'subjects' not in student:
                student['subjects'] = {}
            student['subjects'][subject] = grade
            break

# Задача 7
def remove_subject(students, name, subject):
    for student in students:
        if student['name'] == name:
            if 'subjects' in student and subject in student['subjects']:
                del student['subjects'][subject]
            break

# Задача 8
def update_subject_grade(students, name, subject, new_grade):
    for student in students:
        if student['name'] == name:
            if 'subjects' in student and subject in student['subjects']:
                student['subjects'][subject] = new_grade
            break

# Задача 9
def get_subject_grade(students, name, subject):
    for student in students:
        if student['name'] == name:
            if 'subjects' in student and subject in student['subjects']:
                return student['subjects'][subject]
    return None

# Задача 10
def print_student_subjects(students, name):
    for student in students:
        if student['name'] == name:
            if 'subjects' in student:
                for subject, grade in student['subjects'].items():
                    print(f"Предмет: {subject}, Оценка: {grade}")
            break

# Пример использования функций
students = []

# Добавление студентов
add_student(students, 'Иван', 5)
add_student(students, 'Мария', 4)

# Обновление оценки
update_grade(students, 'Иван', 6)

# Добавление предметов
add_subject(students, 'Иван', 'Математика', 5)
add_subject(students, 'Мария', 'Физика', 4)

# Печать студентов и их оценок
print_students(students)

# Печать предметов и оценок для студента
print_student_subjects(students, 'Иван')

# Удаление предмета
remove_subject(students, 'Иван', 'Математика')

# Удаление студента
remove_student(students, 'Мария')

# Печать студентов после удалений
print_students(students)
