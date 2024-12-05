# Описание: Напишите функцию rectangle_area(length, width), которая принимает длину и ширину прямоугольника и возвращает его площадь.
# Формула: Площадь прямоугольника = длина * ширина
def rectangle_area(length, width):
    return length * width

length = int(input("Введите длину: "))
width = int(input("Введите ширину: "))
print("Площадь прямоугольника:", rectangle_area(length, width))

# Описание: Напишите функцию triangle_area(base, height), которая принимает основание и высоту треугольника и возвращает его площадь.
# Формула: Площадь треугольника = 0.5 * основание * высота
def triangle_area(base, height):
    return 0.5 * base * height

base = int(input("Введите основание: "))
height = int(input("Введите высоту: "))
print("Площадь треугольника:", triangle_area(base, height))


# Описание: Напишите функцию circle_area(radius), которая принимает радиус круга и возвращает его площадь.
# Формула: Площадь круга = π * радиус^2

def circle_area(radius):
    return 3.1415 * (radius ** 2)

radius = int(input("Введите радиус: "))
print("Площадь круга:", circle_area(radius))

# Описание: Напишите функцию fahrenheit_to_celsius(fahrenheit), которая принимает температуру в градусах Фаренгейта и возвращает её в градусах Цельсия.
# Формула: Температура в Цельсиях = (температура в Фаренгейтах - 32) * 5 / 9

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

fahrenheit = int(input("Введите температуру в Фаренгейтах: "))
print("Температура в Цельсиях:", fahrenheit_to_celsius(fahrenheit))

# Описание: Напишите функцию celsius_to_fahrenheit(celsius), которая принимает температуру в градусах Цельсия и возвращает её в градусах Фаренгейта.
# Формула: Температура в Фаренгейтах = температура в Цельсиях * 9 / 5 + 32
def celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32

celsius = int(input("Введите температуру в Цельсиях: "))
print("Температура в Фаренгейтах:", celsius_to_fahrenheit(celsius))



# Напишите функцию bmi(weight, height), которая принимает вес (в килограммах) и рост (в метрах) и возвращает индекс массы тела (BMI).
# Формула: Индекс массы тела (BMI) = вес / рост^2
def bmi(weight, height):
    return weight / (height ** 2)

weight = float(input("Введите вес в килограммах: "))
height = float(input("Введите рост в метрах: "))
print("Индекс массы тела (BMI):", bmi(weight, height))


# Описание: Напишите функцию loan_payment(principal, annual_rate, months), которая рассчитывает ежемесячный платеж по кредиту с фиксированной процентной ставкой.

# Формула: Ежемесячный платеж = (principal * (monthly_rate / 100)) / (1 - (1 + monthly_rate / 100) ^ -months)
# где monthly_rate = annual_rate / 12

def loan_payment(principal, annual_rate, months):
    monthly_rate = annual_rate / 12
    numerator = principal * (monthly_rate / 100)
    denominator = 1 - (1 + monthly_rate / 100) ** -months
    return numerator / denominator

principal = float(input("Введите сумму кредита: "))
annual_rate = float(input("Введите годовую процентную ставку: "))
months = int(input("Введите срок кредита в месяцах: "))
print("Ежемесячный платеж:", loan_payment(principal, annual_rate, months))

