# Task 1
books = ["Гарри Поттер", "Властелин колец", "Шерлок Холмс", "1984", "Мастер и Маргарита"]
for book in books:
    print(f'"{book}"')

# Task 2
numbers = [2, 4, 6, 8, 10, 12]
for number in numbers:
    print(f"{number} и его удвоенное значение {number * 2}")

# Task 3
fruits = ["яблоко", "банан", "апельсин", "груша", "слива", "вишня", "манго", "киви"]
for i, fruit in enumerate(fruits, 1):
    print(f"{i}. {fruit}")

# Task 4
animals = ["кошка", "собака", "тигр", "лев", "жираф", "слон", "зебра", "обезьяна", "панда", "волк"]
for animal in animals:
    print(animal.upper())

# Task 5
numbers = [1, 2, 3, 4, 5]
for number in numbers:
    print(f"{number} в квадрате {number ** 2}")

# Task 6
words = ["мама", "море", "машина", "дом", "окно", "молоко", "вода"]
for word in words:
    if word.startswith("м"):
        print(word)

# Task 7
cities = ["Москва", "Париж", "Лондон", "Токио", "Нью-Йорк", "Берлин", "Мадрид", "Рим", "Сидней", "Дели"]
for city in cities:
    if "а" in city:
        print(city)

# Task 8
numbers = [1, 2, 3, 4, 5, 6]
product = 1
for number in numbers:
    product *= number
print(product)

# Task 9
friends = ["Алексей", "Мария", "Иван", "Анна", "Дмитрий", "Елена", "Сергей", "Ольга"]
for friend in friends:
    print(friend[::-1])

# Task 10
drinks = ["вода", "сок", "чай", "кофе", "молоко"]
for drink in drinks:
    print(drink * 2)

# Task 11
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for number in numbers:
    if number % 2 != 0:
        print(number)

# Task 12
colors = ["красный", "синий", "зеленый", "желтый", "фиолетовый", "белый", "черный"]
for color in colors:
    print(f"{color} - это цвет")

# Task 13
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum_numbers = sum(numbers)
print(sum_numbers)

# Task 14
movies = ["Гарри Поттер", "Матрица", "Интерстеллар", "Начало", "Властелин колец"]
for i, movie in enumerate(movies, 1):
    print(f"{i}. {movie}")

# Task 15
numbers = [1, 2, 3, 4, 5, 6]
for number in numbers:
    print(f"{number} в кубе {number ** 3}")

# Task 16
words = ["слово", "абракадабра", "дом", "машина", "коллекция", "предложение", "человек", "стол"]
for word in words:
    if len(word) > 3:
        print(word)

# Task 17
animals = ["кошка", "собака", "тигр", "лев", "жираф", "слон", "зебра"]
for animal in animals:
    print(f"{animal} - это животное")

# Task 18
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for number in numbers:
    if number % 3 == 0:
        print(number)

# Task 19
countries = ["Россия", "США", "Канада", "Франция", "Германия", "Япония"]
for country in countries:
    print(country.lower())

# Task 20
numbers = [2, 4, 6, 8, 10, 12, 14, 16]
average = sum(numbers) / len(numbers)
print(average)
