
# Task 1
students = {"Alice": 20, "Bob": 17, "Charlie": 19}
for name, age in students.items():
    if age > 18:
        print(f"{name}: Совершеннолетний")
    else:
        print(f"{name}: Несовершеннолетний")

# Task 2
students = {"Alice": 20, "Bob": 17, "Charlie": 19}
key = input("Введите имя студента: ")
if key in students:
    print(f"{key}: {students[key]}")
else:
    print("Ключ не найден")

# Task 3
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = []
for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)
print(even_numbers)

# Task 4
fruits = ["яблоко", "банан", "вишня"]
fruit = input("Введите название фрукта: ")
if fruit in fruits:
    print("Фрукт найден")
else:
    print("Фрукт не найден")

# Task 5
items = {"Книга": 150, "Ручка": 50, "Тетрадь": 30}
for item, price in items.items():
    if price > 100:
        print(f"{item}: Дорогой предмет")
    else:
        print(f"{item}: Дешевый предмет")

# Task 6
students = {"Alice": 20, "Bob": 17, "Charlie": 19}
name = input("Введите имя студента: ")
if name in students:
    del students[name]
    print(f"{name} удален из словаря")
else:
    print("Студент не найден")

# Task 7
numbers = []
number = int(input("Введите число: "))
if number > 10:
    numbers.append(number)
elif number < 5:
    print("Слишком мало")

# Task 8
strings = ["hello", "world", "python", "is", "fun"]
for i in range(len(strings)):
    if len(strings[i]) > 5:
        strings[i] = "Длинная строка"
print(strings)

# Task 9
grade = int(input("Введите оценку студента: "))
if grade > 75:
    print("Отлично")
elif grade >= 50:
    print("Хорошо")
else:
    print("Плохо")

# Task 10
students = {"Alice": 85, "Bob": 78, "Charlie": 90}
for name, grade in students.items():
    if grade > 80:
        print(f"{name}: Отличник")

# Task 11
weekday = input("Введите день недели: ").lower()
if weekday in ["понедельник", "вторник", "среда"]:
    print("Рабочий день")
elif weekday in ["суббота", "воскресенье"]:
    print("Выходной")

# Task 12
numbers = [1, -2, 3, -4, 5, 6]
positive_numbers = []
for number in numbers:
    if number > 0:
        positive_numbers.append(number)
    elif number < 0:
        print(f"{number}: Отрицательное число")
print(positive_numbers)

# Task 13
colors = ["красный", "зеленый", "синий"]
color = input("Введите название цвета: ").lower()
if color in colors:
    print("Основной цвет")
else:
    print("Дополнительный цвет")

# Task 14
cities = {"Москва": 12506468, "Санкт-Петербург": 5351935, "Новосибирск": 1620162}
for city, population in cities.items():
    if population > 1000000:
        print(f"{city}: Мегаполис")
    else:
        print(f"{city}: Город")

# Task 15
employees = ["Alice", "Bob", "Charlie"]
name = input("Введите имя сотрудника: ")
if name in employees:
    employees.remove(name)
    print(f"{name} удален из списка")
else:
    employees.append(name)
    print(f"{name} добавлен в список")

# Task 16
numbers = [1, 2, 3, 4, 5, 15]
for i in range(len(numbers)):
    if numbers[i] % 3 == 0 and numbers[i] % 5 == 0:
        numbers[i] = "FizzBuzz"
    elif numbers[i] % 3 == 0:
        numbers[i] = "Fizz"
    elif numbers[i] % 5 == 0:
        numbers[i] = "Buzz"
print(numbers)

# Task 17
temperature = int(input("Введите температуру: "))
if temperature > 30:
    print("Жарко")
elif temperature >= 10:
    print("Тепло")
else:
    print("Холодно")

# Task 18
months = {"Январь": 31, "Февраль": 28, "Март": 31, "Апрель": 30}
for month, days in months.items():
    if days == 31:
        print(f"{month}: Длинный месяц")
    else:
        print(f"{month}: Короткий месяц")

# Task 19
number = int(input("Введите число: "))
if number % 2 == 0:
    print("Четное")
else:
    print("Нечетное")

# Task 20
strings = ["apple", "banana", "avocado", "grape", "apricot"]
new_strings = []
for string in strings:
    if string[0].lower() == "а":
        new_strings.append(string)
print(new_strings)