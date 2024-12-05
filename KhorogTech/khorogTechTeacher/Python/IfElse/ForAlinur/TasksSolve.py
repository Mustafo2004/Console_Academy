# 1. Age check
age = 14
if age < 13:
    print("Ребенок")
elif 13 <= age <= 18:
    print("Подросток")
else:
    print("Взрослый")

# 2. Season check
season = "зима"
if season == "зима":
    print("Зима")
elif season == "лето":
    print("Лето")
elif season == "весна":
    print("Весна")
else:
    print("Осень")

# 3. Number check
num = -5
if num > 0:
    if num % 2 == 0:
        print("Положительное четное число")
    else:
        print("Положительное нечетное число")
elif num < 0:
    print("Отрицательное число")
else:
    print("Ноль")

# 4. Grade check
grade = 85
if grade >= 90:
    print("Отлично")
elif 80 <= grade < 90:
    print("Хорошо")
elif 70 <= grade < 80:
    print("Удовлетворительно")
else:
    print("Неудовлетворительно")

# 5. Season cold/warm check
season = "лето"
if season == "лето" or season == "зима":
    print("Холодно")
else:
    print("Тепло")

# 6. License check
age = 20
has_license = True
if age >= 18 and has_license:
    print("Можно получить водительские права")
elif age >= 18 and not has_license:
    print("Нет прав, но можно получить")
else:
    print("Не достигнут возраст для прав")

# 7. Payment method check
payment_method = "карта"
if payment_method == "карта":
    print("Оплата картой")
elif payment_method == "наличные":
    print("Оплата наличными")
elif payment_method == "чек":
    print("Оплата чеком")
else:
    print("Неизвестный способ оплаты")

# 8. Weekday check
weekday = "понедельник"
if weekday == "понедельник":
    print("Первый рабочий день недели")
elif weekday == "вторник":
    print("Второй рабочий день недели")
elif weekday == "среда":
    print("Середина недели")
elif weekday == "четверг":
    print("Почти конец недели")
elif weekday == "пятница":
    print("Пятница - последний рабочий день недели")
else:
    print("Выходные дни")

# 9. Score check
score = 75
if score >= 90:
    print("Оценка A")
elif 80 <= score < 90:
    print("Оценка B")
elif 70 <= score < 80:
    print("Оценка C")
elif 60 <= score < 70:
    print("Оценка D")
else:
    print("Оценка F")

# 10. Purchase amount check
amount = 45
if amount >= 100:
    print("Сумма со скидкой")
elif 50 <= amount < 100:
    print("Сумма со скидкой")
else:
    print("Сумма без скидки")

# 11. Speed check
speed = 60
if speed > 100:
    print("Очень быстро!")
elif 51 <= speed <= 100:
    print("Средняя скорость")
else:
    print("Медленно двигаемся")

# 12. Leap year check
year = 2024
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("Високосный год")
else:
    print("Не високосный год")

# 13. Time of day check
time_of_day = 15
if 6 <= time_of_day < 12:
    print("Утро")
elif 12 <= time_of_day < 18:
    print("День")
elif 18 <= time_of_day < 24:
    print("Вечер")
else:
    print("Ночь")

# 14. Role check
role = "admin"
if role == "admin":
    print("Доступ разрешен")
elif role == "user":
    print("Доступ ограничен")
else:
    print("Доступ запрещен")

# 15. Account status check
is_active = True
if is_active:
    print("Активный аккаунт")
else:
    print("Неактивный аккаунт")

# 16. Result check
result = 1
if result > 0:
    print("Победа")
elif result == 0:
    print("Ничья")
else:
    print("Поражение")

# 17. Hour check
hour = 20
if 6 <= hour < 12:
    print("Утро")
elif 12 <= hour < 18:
    print("День")
elif 18 <= hour < 24:
    print("Вечер")
else:
    print("Ночь")

# 18. Weekend check
date = "воскресенье"
if date == "суббота" or date == "воскресенье":
    print("Выходной день!")
else:
    print("Рабочий день")

# 19. Programming language check
language = "Python"
if language == "Python":
    print("Python")
elif language == "JavaScript":
    print("JavaScript")
elif language == "Java":
    print("Java")
else:
    print("Другой язык")

# 20. Month check
month = "апрель"
if month in ["март", "апрель", "май"]:
    print("Это весна")
elif month in ["июнь", "июль", "август"]:
    print("Это лето")
elif month in ["сентябрь", "октябрь", "ноябрь"]:
    print("Это осень")
else:
    print("Это зима")
