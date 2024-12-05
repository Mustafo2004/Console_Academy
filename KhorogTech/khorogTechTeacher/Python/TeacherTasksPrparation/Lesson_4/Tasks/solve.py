# Задача 1
def check_even_or_odd():
    number = int(input("Введите число: "))
    if number % 2 == 0:
        print("Четное число")
    else:
        print("Нечетное число")

# Задача 2
def check_day_of_week():
    day = input("Введите день недели: ").strip().lower()
    if day == "понедельник":
        print("Начало недели")
    elif day == "пятница":
        print("Почти выходные")
    elif day in ["суббота", "воскресенье"]:
        print("Выходные")
    else:
        print("Неизвестный день")

# Задача 3
def check_working_age():
    age = int(input("Введите возраст: "))
    if 18 <= age <= 65:
        print("Работоспособный возраст")
    else:
        print("Не работоспособный возраст")

# Задача 4
def check_exam_score():
    score = int(input("Введите количество баллов: "))
    if score >= 60:
        print("Сдал")
    else:
        print("Не сдал")

# Задача 5
def check_number_in_range():
    number = int(input("Введите число: "))
    if 10 <= number <= 50:
        print("В диапазоне")
    else:
        print("Вне диапазона")

# Задача 6
def check_positive_or_negative():
    number = int(input("Введите число: "))
    if number > 0:
        print("Положительное число")
    elif number < 0:
        print("Отрицательное число")
    else:
        print("Ноль")

# Задача 7
def check_divisibility():
    number = int(input("Введите число: "))
    if number % 3 == 0 and number % 5 == 0:
        print("Кратно 3 и 5")
    elif number % 3 == 0:
        print("Кратно 3")
    elif number % 5 == 0:
        print("Кратно 5")
    else:
        print("Не кратно ни 3, ни 5")

# Задача 8
def check_less_than_100():
    number = int(input("Введите число: "))
    if number < 100:
        print("Меньше 100")
    else:
        print("Больше или равно 100")

# Задача 9
def check_time_of_day():
    hour = int(input("Введите время в часах (0-23): "))
    if 0 <= hour <= 11:
        print("Утро")
    elif 12 <= hour <= 17:
        print("День")
    elif 18 <= hour <= 23:
        print("Вечер")
    else:
        print("Некорректное время")

# Задача 10
def check_age_category():
    age = int(input("Введите возраст: "))
    if age < 13:
        print("Детский возраст")
    else:
        print("Не детский возраст")

if __name__ == "__main__":
    print("Задача 1:")
    check_even_or_odd()
    print("\nЗадача 2:")
    check_day_of_week()
    print("\nЗадача 3:")
    check_working_age()
    print("\nЗадача 4:")
    check_exam_score()
    print("\nЗадача 5:")
    check_number_in_range()
    print("\nЗадача 6:")
    check_positive_or_negative()
    print("\nЗадача 7:")
    check_divisibility()
    print("\nЗадача 8:")
    check_less_than_100()
    print("\nЗадача 9:")
    check_time_of_day()
    print("\nЗадача 10:")
    check_age_category()




age = int(input("Введите возраст пользователя: "))
book_type = input("Введите тип книги (художественная, научная, учебная): ").strip().lower()

if book_type == "художественная":
    if age < 12:
        print("Не рекомендуется для детей")
    elif age <= 18:
        print("Подходит для подростков")
    else:
        print("Подходит для взрослых")
elif book_type == "научная":
    if age < 12:
        print("Не рекомендуется для детей")
    else:
        print("Подходит для всех возрастов")
elif book_type == "учебная":
    if age < 12:
        print("Подходит для детей")
    else:
        print("Подходит для всех возрастов")
else:
    print("Неверный тип книги")
