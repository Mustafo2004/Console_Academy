# Task 1
age = int(input("Введите возраст: "))
if age < 18:
    print("Несовершеннолетний")
elif 18 <= age <= 65:
    print("Взрослый")
else:
    print("Пожилой")

# Task 2
number = int(input("Введите число: "))
if number > 100:
    print("Большое число")
elif number == 100:
    print("Равно 100")
else:
    print("Маленькое число")

# Task 3
name = input("Введите имя: ")
if name.startswith("А"):
    print("Имя начинается с А")
else:
    print("Имя не начинается с А")

# Task 4
temperature = int(input("Введите температуру в градусах Цельсия: "))
if temperature < 0:
    print("Мороз")
elif 0 <= temperature <= 20:
    print("Прохладно")
else:
    print("Тепло")

# Task 5
number = int(input("Введите число: "))
if number % 2 == 0:
    print("Четное число")
else:
    print("Нечетное число")

# Task 6
month = input("Введите название месяца: ").lower()
if month in ["июнь", "июль", "август"]:
    print("Летний месяц")
elif month in ["декабрь", "январь", "февраль"]:
    print("Зимний месяц")
else:
    print("Не летний и не зимний месяц")

# Task 7
grade = int(input("Введите оценку от 1 до 5: "))
if grade == 5:
    print("Отлично")
elif grade == 4:
    print("Хорошо")
elif grade == 3:
    print("Удовлетворительно")
else:
    print("Неудовлетворительно")

# Task 8
day = input("Введите день недели: ").lower()
if day in ["суббота", "воскресенье"]:
    print("Выходной день")
else:
    print("Рабочий день")

# Task 9
number = int(input("Введите число: "))
if number > 0:
    print("Положительное число")
elif number < 0:
    print("Отрицательное число")
else:
    print("Число равно нулю")

# Task 10
string = input("Введите строку: ")
if len(string) > 10:
    print("Длинная строка")
elif len(string) < 5:
    print("Короткая строка")
else:
    print("Строка средней длины")

# Task 11
hour = int(input("Введите текущий час (от 0 до 23): "))
if 6 <= hour <= 11:
    print("Утро")
elif 12 <= hour <= 17:
    print("День")
elif 18 <= hour <= 23:
    print("Вечер")
else:
    print("Ночь")

# Task 12
purchase_amount = float(input("Введите сумму покупки: "))
if purchase_amount > 1000:
    print("Скидка 10%")
elif purchase_amount > 500:
    print("Скидка 5%")
else:
    print("Скидка не предоставляется")

# Task 13
password = input("Введите пароль: ")
if len(password) < 8:
    print("Пароль слишком короткий")
elif password.isalpha():
    print("Пароль должен содержать цифры")
else:
    print("Пароль принят")

# Task 14
age = int(input("Введите возраст: "))
if age < 7:
    print("Дошкольник")
elif 7 <= age <= 17:
    print("Школьник")
elif 18 <= age <= 22:
    print("Студент")
else:
    print("Взрослый")

# Task 15
number = int(input("Введите число: "))
if number % 3 == 0 and number % 5 == 0:
    print("Делится на 3 и 5")
elif number % 3 == 0:
    print("Делится на 3")
elif number % 5 == 0:
    print("Делится на 5")
else:
    print("Не делится ни на 3, ни на 5")

# Task 16
ege_score = int(input("Введите баллы ЕГЭ: "))
if ege_score > 90:
    print("Отличный результат")
elif 70 <= ege_score <= 90:
    print("Хороший результат")
elif 50 <= ege_score <= 69:
    print("Удовлетворительный результат")
else:
    print("Низкий результат")

# Task 17
speed = int(input("Введите скорость автомобиля: "))
if speed < 60:
    print("Низкая скорость")
elif 60 <= speed <= 120:
    print("Средняя скорость")
else:
    print("Высокая скорость")

# Task 18
employee_count = int(input("Введите количество сотрудников: "))
if employee_count < 10:
    print("Маленькая компания")
elif 10 <= employee_count <= 100:
    print("Средняя компания")
else:
    print("Большая компания")

# Task 19
length = float(input("Введите длину отрезка: "))
if length < 1:
    print("Маленький отрезок")
elif 1 <= length <= 5:
    print("Средний отрезок")
else:
    print("Большой отрезок")

# Task 20
page_count = int(input("Введите количество страниц книги: "))
if page_count < 100:
    print("Короткая книга")
elif 100 <= page_count <= 300:
    print("Средняя книга")
else:
    print("Длинная книга")
