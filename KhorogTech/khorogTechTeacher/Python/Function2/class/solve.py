
# Задача 1
def add_numbers(a, b):
    return a + b

# Задача 2
def subtract_numbers(a, b):
    return a - b

# Задача 3
def multiply_numbers(a, b):
    return a * b

# Задача 4
def divide_numbers(a, b):
    if b != 0:
        return a / b
    else:
        return "Ошибка: деление на ноль"

# Задача 5
def square_number(a):
    return a ** 2

# Задача 6
def cube_number(a):
    return a ** 3

# Задача 7
def power_of_number(base, exponent):
    return base ** exponent

# Задача 8
def average_of_two_numbers(a, b):
    return (a + b) / 2

# Задача 9
def rectangle_area(length, width):
    return length * width

# Задача 10
def rectangle_perimeter(length, width):
    return 2 * (length + width)

# Задача 11
def circle_area(radius):
    return 3.14 * radius ** 2

# Задача 12
def circle_circumference(radius):
    return 2 * 3.14 * radius

# Задача 13
def triangle_area(base, height):
    return 0.5 * base * height

# Задача 14
def triangle_perimeter(a, b, c):
    return a + b + c

# Задача 15
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Задача 16
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Задача 17

# Задача 18
def convert_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Задача 19
def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Задача 20
def simple_interest(principal, rate, time):
    return principal * rate * time / 100
