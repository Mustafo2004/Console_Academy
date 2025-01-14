
# ! Task-1
# Создайте пустой список items. Выполните следующие шаги:
# Добавление элементов: Пользователь должен ввести 3 предмета (например, "ручка", "карандаш", "тетрадь"), которые добавляются в список с помощью метода append.
# Удаление элемента: Пользователь должен ввести один из предметов, который будет удален из списка с помощью метода remove.
# Вставка элемента: Пользователь должен ввести новый предмет, который добавляется в начало списка с помощью метода insert.
# В конце выведите итоговый список.
# ! Task-2
# Создайте список contacts с именами трех контактов (например, "Алексей", "Марина", "Ольга"). Выполните следующие шаги:
# Изменение контакта: Пользователь должен ввести индекс контакта и новое имя, чтобы заменить существующий элемент.
# Добавление нового контакта: Пользователь должен ввести новое имя, которое добавляется в конец списка с помощью метода append.
# Удаление контакта: Пользователь должен ввести имя контакта, который нужно удалить из списка с помощью метода remove.
# Вставка контакта: Пользователь должен ввести новое имя и вставить его на второе место в списке с помощью метода insert.
# ! Task-3
# У вас есть список party_guests, в котором указаны имена четырех гостей, приглашенных на вечеринку (например, "Иван", "Елена", "Максим", "Анна"). Выполните следующие шаги:
# Удаление гостя: Пользователь должен ввести имя гостя, который не сможет прийти на вечеринку, и удалить его из списка с помощью метода remove.
# Вставка нового гостя: Пользователь должен ввести имя нового гостя и указать индекс, на который его нужно добавить в список с помощью метода insert.
# Изменение гостя: Пользователь должен выбрать гостя по индексу и изменить его имя на новое, указанное пользователем.
# Добавление гостей: Пользователь должен ввести два дополнительных имени, которые добавляются в конец списка с помощью метода append.
#! Task-4
# Создайте словарь с именем product, который содержит следующие ключи и значения:
# name: "Laptop"
# price: 1500
# stock: 25
# Попросите пользователя ввести новое значение для ключа price и обновите это значение в словаре.
# Попросите пользователя ввести количество товара для продажи и уменьшите значение ключа stock на это количество.
# удалите ключ stock из словаря, используя метод pop.
# Выведите обновленный словарь на экран.
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

#! Task-5
# Создайте словарь с именем user, который содержит следующие ключи и значения:
# username: "user123"
# email: "user123@example.com"
# password: "pass123"
# Попросите пользователя изменить значение ключа username. Обновите это значение в словаре.
# Затем попросите пользователя ввести новый пароль и обновите значение ключа password.
# удалите ключ email из словаря, используя метод pop.
# Выведите обновленный словарь на экран.

#! Task-6
# Создайте словарь, который хранит информацию о трех книгах в библиотеке. Для каждой книги у вас должен быть вложенный словарь, содержащий следующие данные:
# Название книги
# Автор
# Год публикации
# Задание:
# Добавьте новую книгу в словарь, используя метод update.
# Удалите одну из книг с помощью метода pop и выведите на экран название и автора второй книги.
#! Task-7
# Создайте словарь, который хранит информацию о трех студентах. Для каждого студента должен быть вложенный словарь, содержащий следующие данные:
#? Example
students = {
    "student_1": {"name": "Алексей", "age": 20, "average_grade": 4.5},
    "student_2": {"name": "Мария", "age": 19, "average_grade": 4.7},
    "student_3": {"name": "Иван", "age": 21, "average_grade": 4.2}
}
# Имя
# Возраст
# Средний балл
# Задание:
# Добавьте информацию о новом студенте с помощью метода update.
# Измените возраст одного из студентов
#  удалите студент используя метод pop.


# !
# Создайте список с тремя словарями, каждый из которых содержит ключи "имя" и "возраст".
# Обновите возраст второго словаря в списке.
# Выведите обновленный список на экран.

# ! Task-8
# Управление списком книг
# Шаг 1: Создайте список книг, где каждая книга представлена в виде словаря с ключами title и author.
# Шаг 2: Выведите на экран список книг, чтобы увидеть текущие книги.
# Шаг 3: Запросите у пользователя название новой книги и имя автора.
# Шаг 4: Добавьте новую книгу в список на основе введенных пользователем данных.
# Шаг 5: Выведите обновленный список книг на экран.
# Шаг 1: Создайте список книг
books = [
    {'title': '1984', 'author': 'George Orwell'},
    {'title': 'To Kill a Mockingbird', 'author': 'Harper Lee'},
    {'title': 'The Great Gatsby', 'author': 'F. Scott Fitzgerald'}
]

# Шаг 2: Выведите на экран список книг
print("Текущий список книг:")
for book in books:
    print(f"Название: {book['title']}, Автор: {book['author']}")

# Шаг 3: Запросите у пользователя название новой книги и имя автора
new_title = input("Введите название новой книги: ")
new_author = input("Введите имя автора новой книги: ")

# Шаг 4: Добавьте новую книгу в список
new_book = {'title': new_title, 'author': new_author}
books.append(new_book)

# Шаг 5: Выведите обновленный список книг на экран
print("\nОбновленный список книг:")
for book in books:
    print(f"Название: {book['title']}, Автор: {book['author']}")


# ! Task-9
# Управление списком сотрудников
# Шаг 1: Создайте список сотрудников, где каждый сотрудник представлен в виде словаря с ключами name и position.
# Шаг 2: Выведите текущий список сотрудников.
# Шаг 3: Запросите у пользователя имя нового сотрудника и его должность.
# Шаг 4: Добавьте нового сотрудника в список.
# Шаг 5: Выведите обновленный список сотрудников.

# ! Task-10
# Задача: Управление списком студентов
# 1. Шаг 1: Вывести текущий список студентов.
students = [
    {"name": "Alex", "math_grade": 85},
    {"name": "Maria", "math_grade": 92},
    {"name": "John", "math_grade": 78}
]
# У вас есть список студентов, где каждый студент представлен в виде словаря. Первый шаг — вывести этот список на экран, чтобы увидеть текущих студентов и их оценки.
# 2. Шаг 2: Добавить нового студента в список.
# Создайте новый словарь, представляющий студента, с именем и оценкой по математике. Затем добавьте этот новый словарь в список студентов, используя соответствующий метод.
# 3. Шаг 3: Запросить данные у пользователя для добавления нового студента.
# Попросите пользователя ввести имя нового студента и его оценку по математике. Используйте эти данные для создания нового словаря студента, который нужно добавить в список.
# 4. Шаг 4: Добавить нового студента в список на основе данных пользователя.
# Возьмите данные, введенные пользователем, и создайте на их основе словарь нового студента. Добавьте этот словарь в список студентов.
# 5. Шаг 5: Вывести обновленный список студентов.
# После добавления нового студента, снова выведите список студентов на экран, чтобы увидеть обновленный список с добавленным студентом

# ! Task-11
# Создание пустого списка
# Добавьте в список students первого студента с помощью метода append(). Первый словарь должен содержать имя, возраст и оценки по математике и английскому языку.
# Добавление второго студента
# Добавьте второго студента с помощью метода append(). Его данные также включают имя, возраст и оценки.
# Удаление студента с помощью метода remove
# Обновление данных студента с помощью метода update
# Представьте, что оценки одного из студентов нужно обновить. Используйте метод update() для изменения оценок по математике для второго студента.
# Создание пустого списка
students = []

# Добавьте в список первого студента с помощью метода append()
students.append({
    'name': 'Anna',
    'age': 14,
    'math_score': 85,
    'english_score': 90
})

# Добавление второго студента
students.append({
    'name': 'Ivan',
    'age': 15,
    'math_score': 78,
    'english_score': 88
})

# Удаление студента с помощью метода remove
# Удалим первого студента (Anna)
students.remove(students[0])

# Обновление данных студента с помощью метода update
# Обновление оценки по математике для второго студента (Ivan)
students[0].update({'math_score': 92})

# Вывод списка студентов после всех операций
print(students)


# ! Task-12
# Создайте пустой список menu, который будет содержать информацию о блюдах ресторана.
# Добавьте первое блюдо в menu с информацией о его цене и шеф-поваре (вложенный словарь с именем и рейтингом).
# Добавьте второе блюдо в меню, указав его название, цену и информацию о шеф-поваре.
# Удалите одно из блюд из меню. Например, удалите "Том Ям".
# Обновите цену блюда "Ризотто с грибами" с помощью метода update()
#? menu[0].update({"price": 650})
# Создайте пустой список menu
menu = []

# Добавьте первое блюдо в menu с информацией о его цене и шеф-поваре
menu.append({
    'dish': 'Том Ям',
    'price': 500,
    'chef': {
        'name': 'Иван Иванов',
        'rating': 4.8
    }
})

# Добавьте второе блюдо в меню
menu.append({
    'dish': 'Ризотто с грибами',
    'price': 650,
    'chef': {
        'name': 'Анна Петрова',
        'rating': 4.9
    }
})

# Удалите одно из блюд, например, "Том Ям" (это первый элемент списка)
menu.pop(0)

# Обновите цену блюда "Ризотто с грибами" (это теперь первое блюдо в списке)
menu[0].update({'price': 700})

# Вывод меню после всех операций
print(menu)


# ! Task-13

# Задача 1: Информация о фильмах с insert() и pop()
# Создайте пустой список movies, который будет содержать информацию о фильмах.
# Добавьте первый фильм в список movies с помощью метода insert(), указав название, год выпуска и режиссера (вложенный словарь с именем и национальностью).
# Добавьте второй фильм в список, указав его название, год выпуска и информацию о режиссере, также с помощью метода insert() (добавьте его в начало списка).
# Удалите фильм с конца списка с помощью метода pop().
# Обновите год выпуска фильма "Интерстеллар" с помощью метода update()

# Создайте пустой список movies
movies = []

# Добавьте первый фильм с помощью метода insert()
movies.insert(0, {
    'title': 'Властелин колец',
    'year': 2001,
    'director': {
        'name': 'Питер Джексон',
        'nationality': 'Новая Зеландия'
    }
})

# Добавьте второй фильм в начало списка с помощью метода insert()
movies.insert(0, {
    'title': 'Интерстеллар',
    'year': 2014,
    'director': {
        'name': 'Кристофер Нолан',
        'nationality': 'Великобритания'
    }
})

# Удалите фильм с конца списка с помощью метода pop()
movies.pop()

# Обновите год выпуска фильма "Интерстеллар"
movies[0].update({'year': 2016})

# Вывод списка фильмов
print(movies)





