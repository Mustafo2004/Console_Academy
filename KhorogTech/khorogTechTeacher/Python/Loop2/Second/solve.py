# Task 1
friends = ["Алексей", "Мария", "Иван", "Анна", "Дмитрий"]
for friend in friends:
    print(friend)

# Task 2
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for number in numbers:
    print(number * 2)

# Task 3
rainbow_colors = ["Красный", "Оранжевый", "Желтый", "Зеленый", "Голубой", "Синий", "Фиолетовый"]
for color in rainbow_colors:
    print(color)

# Task 4
favorite_dishes = ["Пицца", "Суши", "Бургер", "Паста", "Торт", "Мороженое", "Салат", "Суп"]
for i, dish in enumerate(favorite_dishes, 1):
    print(f"{i}. {dish}")

# Task 5
room_items = ["Кровать", "Стол", "Стул", "Шкаф", "Компьютер"]
for item in room_items:
    print(item[::-1])

# Task 6
animals = ["Кошка", "Собака", "Лев", "Тигр", "Слон", "Жираф"]
for animal in animals:
    print(f"{animal} - это животное")

# Task 7
cities = ["Москва", "Нью-Йорк", "Лондон", "Париж", "Токио"]
for city in cities:
    print(city.upper())

# Task 8
numbers = [1, 2, 3, 4, 5, 6, 7]
for number in numbers:
    if number % 2 == 0:
        print(number)

# Task 9
words = ["яблоко", "банан", "виноград", "ананас", "груша", "слива", "апельсин", "арбуз"]
for word in words:
    if "а" in word:
        print(word)

# Task 10
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum_numbers = 0
for number in numbers:
    sum_numbers += number
print(sum_numbers)

# Task 11
movies = ["Гарри Поттер", "Матрица", "Интерстеллар", "Начало", "Властелин колец"]
for movie in movies:
    print(f'"{movie}"')

# Task 12
numbers = [1, 2, 3, 4, 5, 6]
for number in numbers:
    print(f"{number} и его квадрат {number ** 2}")

# Task 13
friends = ["Алексей", "Мария", "Иван", "Анна", "Дмитрий", "Елена", "Сергей", "Ольга"]
for friend in friends:
    print(friend[0])

# Task 14
words = ["дом", "школа", "машина", "море", "дерево"]
for word in words:
    print(word * 2)

# Task 15
numbers = [1, 2, 3, 4, 5, 6, 7]
for number in numbers:
    if number > 5:
        print(number)

# Task 16
words = ["дружба", "любовь", "вера", "надежда", "доброта", "честность", "смелость", "милосердие", "правда", "честь"]
for word in words:
    if len(word) > 4:
        print(word)

# Task 17
numbers = [1, 2, 3, 4, 5, 6]
max_number = max(numbers)
print(max_number)

# Task 18
countries = ["Россия", "США", "Великобритания", "Франция", "Япония"]
for country in countries:
    print(country.lower())

# Task 19
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
sum_numbers = sum(numbers)
average = sum_numbers / len(numbers)
print(average)

# Task 20
names = ["Алексей", "Мария", "Иван", "Анна", "Дмитрий", "Елена", "Сергей"]
for name in names:
    print(f"{name} - это имя")
