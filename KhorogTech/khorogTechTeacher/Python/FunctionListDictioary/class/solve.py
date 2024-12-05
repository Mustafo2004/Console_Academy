def add_student(students, name):
    students.append(name)

def remove_student(students, name):
    if name in students:
        students.remove(name)

def student_count(students):
    return len(students)

def add_grade(grades, name, grade):
    grades[name] = grade

def get_grade(grades, name):
    return grades.get(name, None)

def average_grade(grades):
    return sum(grades.values()) / len(grades) if grades else 0

def students_with_grade(grades, grade):
    return [name for name, g in grades.items() if g == grade]

def highest_grade(grades):
    return max(grades, key=grades.get) if grades else None

def student_exists(students, name):
    return name in students

def grade_exists(grades, name):
    return name in grades

def remove_grade(grades, name):
    if name in grades:
        del grades[name]

def clear_grades(grades):
    grades.clear()

def list_students(students):
    return students

def list_grades(grades):
    return list(grades.values())

def students_with_highest_grade(grades):
    if not grades:
        return []
    highest = max(grades.values())
    return [name for name, grade in grades.items() if grade == highest]

def add_students(students, new_students):
    students.extend(new_students)

def add_grades(grades, new_grades):
    grades.update(new_grades)

def get_students_by_grade_range(grades, min_grade, max_grade):
    return [name for name, grade in grades.items() if min_grade <= grade <= max_grade]

def update_grade(grades, name, new_grade):
    if name in grades:
        grades[name] = new_grade

def find_students_by_letter(students, letter):
    return [name for name in students if name.startswith(letter)]


# Примеры использования
students = []
grades = {}

add_student(students, "Алексей")
add_student(students, "Мария")
print(students)  # ['Алексей', 'Мария']

remove_student(students, "Мария")
print(students)  # ['Алексей']

print(student_count(students))  # 1

add_grade(grades, "Алексей", 5)
print(grades)  # {'Алексей': 5}

print(get_grade(grades, "Алексей"))  # 5
print(get_grade(grades, "Мария"))  # None

add_grade(grades, "Мария", 4)
print(average_grade(grades))  # 4.5

print(students_with_grade(grades, 5))  # ['Алексей']

add_grade(grades, "Иван", 5)
print(highest_grade(grades))  # 'Алексей' или 'Иван'

print(student_exists(students, "Алексей"))  # True
print(student_exists(students, "Мария"))  # False

print(grade_exists(grades, "Алексей"))  # True
print(grade_exists(grades, "Мария"))  # True

remove_grade(grades, "Алексей")
print(grades)  # {'Мария': 4, 'Иван': 5}

clear_grades(grades)
print(grades)  # {}

add_student(students, "Мария")
add_student(students, "Иван")
print(list_students(students))  # ['Алексей', 'Мария', 'Иван']

add_grade(grades, "Мария", 4)
add_grade(grades, "Иван", 5)
print(list_grades(grades))  # [4, 5]

print(students_with_highest_grade(grades))  # ['Иван']

new_students = ['Николай', 'Петр']
add_students(students, new_students)
print(students)  # ['Алексей', 'Мария', 'Иван', 'Николай', 'Петр']

new_grades = {'Николай': 3, 'Петр': 4}
add_grades(grades, new_grades)
print(grades)  # {'Мария': 4, 'Иван': 5, 'Николай': 3, 'Петр': 4}

print(get_students_by_grade_range(grades, 3, 4))  # ['Мария', 'Николай', 'Петр']

update_grade(grades, "Мария", 5)
print(grades)  # {'Мария': 5, 'Иван': 5, 'Николай': 3, 'Петр': 4}

print(find_students_by_letter(students, "А"))  # ['Алексей']
