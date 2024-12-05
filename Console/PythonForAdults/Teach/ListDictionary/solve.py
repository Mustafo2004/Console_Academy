
# ! Task-4
# Создание словаря с начальными значениями
product = {
    "name": "Laptop",
    "price": 1500,
    "stock": 25
}

# Обновление значения ключа price
new_price = float(input("Введите новое значение для ключа 'price': "))
product["price"] = new_price

# Уменьшение значения ключа stock
quantity_sold = int(input("Введите количество товара для продажи: "))
product["stock"] -= quantity_sold

# Удаление ключа stock
product.pop("stock", None)

# Вывод обновленного словаря
print("Обновленный словарь:", product)




# !  Task-6
# Создаем словарь, содержащий информацию о трех книгах
library = {
    1: {
        'Название книги': 'Война и мир',
        'Автор': 'Лев Толстой',
        'Год публикации': 1869
    },
    2: {
        'Название книги': 'Преступление и наказание',
        'Автор': 'Федор Достоевский',
        'Год публикации': 1866
    },
    3: {
        'Название книги': 'Мастер и Маргарита',
        'Автор': 'Михаил Булгаков',
        'Год публикации': 1967
    }
}

# Добавляем новую книгу с помощью метода update
library.update({
    4: {
        'Название книги': 'Анна Каренина',
        'Автор': 'Лев Толстой',
        'Год публикации': 1877
    }
})

# Удаляем одну из книг с помощью метода pop
library.pop(3)

# Выводим на экран название и автора второй книги
second_book = library[2]
print(f"Название: {second_book['Название книги']}, Автор: {second_book['Автор']}")

# ! Task-7
# Создаем словарь, содержащий информацию о трех студентах
students = {
    1: {
        'Имя': 'Андрей',
        'Возраст': 17,
        'Средний балл': 4.5
    },
    2: {
        'Имя': 'Ольга',
        'Возраст': 16,
        'Средний балл': 4.7
    },
    3: {
        'Имя': 'Дмитрий',
        'Возраст': 18,
        'Средний балл': 4.3
    }
}

# Добавляем нового студента с помощью метода update
students.update({
    4: {
        'Имя': 'Мария',
        'Возраст': 19,
        'Средний балл': 4.6
    }
})

# Изменяем возраст одного из студентов (например, у студента под номером 1)
students[1]['Возраст'] = 18

# Удаляем студента под номером 3 с помощью метода pop
students.pop(3)

# Выводим обновленный список студентов
for student_id, info in students.items():
    print(f"Студент {student_id}: Имя: {info['Имя']}, Возраст: {info['Возраст']}, Средний балл: {info['Средний балл']}")


# ! Task-8
# Шаг 1: Вывести текущий список студентов
students = [
    {"name": "Alex", "math_grade": 85},
    {"name": "Maria", "math_grade": 92},
    {"name": "John", "math_grade": 78}
]

print("Текущий список студентов:")
print(f"Имя: {students[0]['name']}, Оценка по математике: {students[0]['math_grade']}")
print(f"Имя: {students[1]['name']}, Оценка по математике: {students[1]['math_grade']}")
print(f"Имя: {students[2]['name']}, Оценка по математике: {students[2]['math_grade']}")

# Шаг 2: Добавить нового студента в список
new_student = {"name": "Anna", "math_grade": 90}
students.append(new_student)

# Шаг 3: Запросить данные у пользователя для добавления нового студента
name = input("Введите имя нового студента: ")
math_grade = int(input("Введите оценку по математике: "))

# Шаг 4: Добавить нового студента в список на основе данных пользователя
new_student_user = {"name": name, "math_grade": math_grade}
students.append(new_student_user)

# Шаг 5: Вывести обновленный список студентов
print("Обновленный список студентов:")
print(f"Имя: {students[0]['name']}, Оценка по математике: {students[0]['math_grade']}")
print(f"Имя: {students[1]['name']}, Оценка по математике: {students[1]['math_grade']}")
print(f"Имя: {students[2]['name']}, Оценка по математике: {students[2]['math_grade']}")
print(f"Имя: {students[3]['name']}, Оценка по математике: {students[3]['math_grade']}")
print(f"Имя: {students[4]['name']}, Оценка по математике: {students[4]['math_grade']}")


# ! Task-11
students = []

# Шаг 2: Добавление первого студента
student1 = {"name": "Ivan", "age": 14, "grades": {"math": 4, "english": 5}}
students.append(student1)

# Шаг 3: Добавление второго студента
student2 = {"name": "Anna", "age": 13, "grades": {"math": 5, "english": 4}}
students.append(student2)

# Шаг 4: Удаление студента
students.remove(student1)

# Шаг 5: Возвращение студента
removed_student = students.pop(0)
students.append(removed_student)

# Шаг 6: Обновление оценки
students[1]["grades"].update({"math": 3})

# Шаг 7: Добавление нового предмета
for student in students:
    student["grades"].update({"physics": 4})

# Шаг 8: Удаление предмета
students[1]["grades"].pop("physics")
