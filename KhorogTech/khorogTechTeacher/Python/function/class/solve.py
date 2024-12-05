# Задача 1
def greet():
    return "Привет, мир!"

# Задача 2
def square(num):
    return num ** 2

# Задача 3
def add(a, b):
    return a + b

# Задача 4
def is_even(num):
    return num % 2 == 0

# Задача 5
def max_of_two(a, b):
    return a if a > b else b

# Задача 6
def say_hello(name):
    return f"Привет, {name}!"

# Задача 7
def area_of_rectangle(length, width):
    return length * width

# Задача 8
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Задача 9
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Задача 10
def count_vowels(text):
    vowels = "аеёиоуыэюяАЕЁИОУЫЭЮЯ"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

# Задача 11
def reverse_string(s):
    return s[::-1]

# Задача 12
def is_palindrome(s):
    return s == s[::-1]

# Задача 13
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

# Задача 14
def sum_of_list(lst):
    return sum(lst)

# Задача 15
def average_of_list(lst):
    return sum(lst) / len(lst) if lst else 0

# Задача 16
def min_of_list(lst):
    return min(lst)

# Задача 17
def max_of_list(lst):
    return max(lst)

# Задача 18
def is_anagram(s1, s2):
    return sorted(s1) == sorted(s2)

# Задача 19
def count_words(text):
    return len(text.split())

# Задача 20
def unique_elements(lst):
    return list(set(lst))

# Тестирование функций
results = {
    "Задача 1": greet(),
    "Задача 2": square(3),
    "Задача 3": add(5, 7),
    "Задача 4": is_even(4),
    "Задача 5": max_of_two(3, 5),
    "Задача 6": say_hello("Андрей"),
    "Задача 7": area_of_rectangle(4, 5),
    "Задача 8": factorial(5),
    "Задача 9": is_prime(7),
    "Задача 10": count_vowels("Привет, как дела?"),
    "Задача 11": reverse_string("Привет"),
    "Задача 12": is_palindrome("довод"),
    "Задача 13": fibonacci(7),
    "Задача 14": sum_of_list([1, 2, 3, 4, 5]),
    "Задача 15": average_of_list([1, 2, 3, 4, 5]),
    "Задача 16": min_of_list([1, 2, 3, 4, 5]),
    "Задача 17": max_of_list([1, 2, 3, 4, 5]),
    "Задача 18": is_anagram("кот", "ток"),
    "Задача 19": count_words("Это тестовая строка для подсчета слов."),
    "Задача 20": unique_elements([1, 2, 2, 3, 4, 4, 5]),
}

print(results)
