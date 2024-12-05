# Решение всех задач с вводом в одном файле на Python

# Задача 1
def input_greet():
    name = input("Введите ваше имя: ")
    return f"Привет, {name}!"

# Задача 2
def input_square():
    num = int(input("Введите число: "))
    return num ** 2

# Задача 3
def input_add():
    a = int(input("Введите первое число: "))
    b = int(input("Введите второе число: "))
    return a + b

# Задача 4
def input_is_even():
    num = int(input("Введите число: "))
    return num % 2 == 0

# Задача 5
def input_max_of_two():
    a = int(input("Введите первое число: "))
    b = int(input("Введите второе число: "))
    return a if a > b else b

# Задача 6
def input_area_of_rectangle():
    length = int(input("Введите длину прямоугольника: "))
    width = int(input("Введите ширину прямоугольника: "))
    return length * width

# Задача 7
def input_factorial():
    n = int(input("Введите число: "))
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Задача 8
def input_is_prime():
    n = int(input("Введите число: "))
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Задача 9
def input_count_vowels():
    text = input("Введите строку: ")
    vowels = "аеёиоуыэюяАЕЁИОУЫЭЮЯ"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

# Задача 10
def input_reverse_string():
    s = input("Введите строку: ")
    return s[::-1]

# Задача 11
def input_is_palindrome():
    s = input("Введите строку: ")
    return s == s[::-1]

# Задача 12
def input_fibonacci():
    n = int(input("Введите число: "))
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

# Задача 13
def input_sum_of_list():
    lst = list(map(int, input("Введите числа через пробел: ").split()))
    return sum(lst)

# Задача 14
def input_average_of_list():
    lst = list(map(int, input("Введите числа через пробел: ").split()))
    return sum(lst) / len(lst) if lst else 0

# Задача 15
def input_min_of_list():
    lst = list(map(int, input("Введите числа через пробел: ").split()))
    return min(lst)

# Задача 16
def input_max_of_list():
    lst = list(map(int, input("Введите числа через пробел: ").split()))
    return max(lst)

# Задача 17
def input_is_anagram():
    s1 = input("Введите первую строку: ")
    s2 = input("Введите вторую строку: ")
    return sorted(s1) == sorted(s2)

# Задача 18
def input_count_words():
    text = input("Введите строку: ")
    return len(text.split())

# Задача 19
def input_unique_elements():
    lst = list(map(int, input("Введите числа через пробел: ").split()))
    return list(set(lst))

# Задача 20
def input_check_age():
    age = int(input("Введите ваш возраст: "))
    return "Доступ разрешен" if age >= 18 else "Доступ запрещен"

# Для тестирования функций нужно раскомментировать вызовы функций:
# print(input_greet())
# print(input_square())
# print(input_add())
# print(input_is_even())
# print(input_max_of_two())
# print(input_area_of_rectangle())
# print(input_factorial())
# print(input_is_prime())
# print(input_count_vowels())
# print(input_reverse_string())
# print(input_is_palindrome())
# print(input_fibonacci())
# print(input_sum_of_list())
# print(input_average_of_list())
# print(input_min_of_list())
# print(input_max_of_list())
# print(input_is_anagram())
# print(input_count_words())
# print(input_unique_elements())
# print(input_check_age())
