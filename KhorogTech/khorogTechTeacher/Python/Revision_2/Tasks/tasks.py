
# Task 1
days = []
day = input("Введите название дня недели: ")
if day not in days:
    days.append(day)
else:
    print("День уже в списке")

# Task 2
students = {}
num_students = int(input("Введите количество студентов: "))
for i in range(1, num_students + 1):
    name = input(f"Введите имя студента {i}: ")
    if name in students.values():
        print("Имя уже существует")
    else:
        students[i] = name

# Task 3
numbers = []
number = int(input("Введите число: "))
if number > 50:
    numbers.append(number)
elif number < 10 and number in numbers:
    numbers.remove(number)

# Task 4
fruits = ["яблоко", "банан", "вишня"]
fruit = input("Введите название фрукта: ")
if fruit in fruits:
    fruits.remove(fruit)
else:
    fruits.append(fruit)

# Task 5
countries = {"Россия": "Москва", "Франция": "Париж"}
country = input("Введите название страны: ")
capital = input("Введите столицу страны: ")
if country in countries:
    countries[country] = capital
else:
    countries[country] = capital

# Task 6
numbers = []
number = int(input("Введите число: "))
if number > 100:
    print("Большое число")
elif number < 50:
    numbers.append(number)

# Task 7
people = {}
name = input("Введите имя человека: ")
age = int(input("Введите возраст человека: "))
if age > 18:
    people[name] = age
else:
    print("Несовершеннолетний")

# Task 8
books = {"Гарри Поттер": "Дж.К. Роулинг"}
book = input("Введите название книги: ")
author = input("Введите автора книги: ")
if book in books:
    print("Книга уже существует")
else:
    books[book] = author

# Task 9
temperature = int(input("Введите температуру: "))
season = input("Введите время года: ").lower()
if season == "лето" and temperature > 25:
    print("Тепло")
elif season == "зима" and temperature < 0:
    print("Холодно")

# Task 10
employees = {}
name = input("Введите имя сотрудника: ")
salary = int(input("Введите зарплату сотрудника: "))
if salary > 50000:
    employees[name] = salary
else:
    print("Низкая зарплата")

# Task 11
even_numbers = []
div_by_3 = []
number = int(input("Введите число: "))
if number % 2 == 0:
    even_numbers.append(number)
if number % 3 == 0:
    div_by_3.append(number)

# Task 12
vowel_words = []
consonant_words = []
word = input("Введите слово: ").lower()
if word[0] in "аеёиоуыэюя":
    vowel_words.append(word)
else:
    consonant_words.append(word)

# Task 13
students = {}
excellent_students = {}
poor_students = {}
name = input("Введите имя студента: ")
grade = int(input("Введите оценку студента: "))
if grade > 90:
    excellent_students[name] = grade
elif grade < 60:
    poor_students[name] = grade

# Task 14
cities = {}
megacities = {}
small_cities = {}
city = input("Введите название города: ")
population = int(input("Введите население города: "))
if population > 1000000:
    megacities[city] = population
elif population < 100000:
    small_cities[city] = population

# Task 15
primary_colors = []
secondary_colors = []
color = input("Введите цвет: ").lower()
if color in ["красный", "синий", "зеленый"]:
    primary_colors.append(color)
else:
    secondary_colors.append(color)

# Task 16
countries = {}
large_countries = {}
small_countries = {}
country = input("Введите название страны: ")
population = int(input("Введите население страны: "))
if population > 50000000:
    large_countries[country] = population
elif population < 10000000:
    small_countries[country] = population

# Task 17
adults_with_a = {}
children = {}
name = input("Введите имя: ")
age = int(input("Введите возраст: "))
if age > 18 and name.startswith("А"):
    adults_with_a[name] = age
elif age <= 18:
    children[name] = age

# Task 18
weekdays = []
weekends = []
day = input("Введите день недели: ").lower()
if day in ["суббота", "воскресенье"]:
    weekends.append(day)
else:
    weekdays.append(day)

# Task 19
students = {}
good_students = {}
bad_students = {}
name = input("Введите имя студента: ")
grade = int(input("Введите оценку студента: "))
if grade > 80:
    good_students[name] = grade
elif grade < 50:
    bad_students[name] = grade

# Task 20
domestic_animals = []