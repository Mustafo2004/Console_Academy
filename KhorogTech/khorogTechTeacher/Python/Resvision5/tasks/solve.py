# Task 1: Sum of numbers in a list
def task1():
    numbers = []
    for _ in range(5):
        number = int(input("Введите число: "))
        numbers.append(number)
    total_sum = sum(numbers)
    print(f"Сумма чисел: {total_sum}")

# Task 2: Remove an element from the list
def task2():
    numbers = [10, 20, 30, 40, 50]
    num_to_remove = int(input("Введите число для удаления: "))
    if num_to_remove in numbers:
        numbers.remove(num_to_remove)
        print(f"Обновленный список: {numbers}")
    else:
        print("Число не найдено в списке.")

# Task 3: Average of numbers in a list
def task3():
    numbers = [10, 20, 30, 40, 50]
    total_sum = sum(numbers)
    average = total_sum / len(numbers)
    print(f"Среднее значение: {average}")

# Task 4: Factorial function
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def task4():
    num = int(input("Введите число для вычисления факториала: "))
    print(f"Факториал {num}: {factorial(num)}")

# Task 5: Dictionary with grades
def task5():
    grades = {'Alice': 85, 'Bob': 90, 'Charlie': 78}
    print(f"Исходный словарь: {grades}")
    new_student = input("Введите имя нового студента: ")
    new_grade = int(input("Введите оценку нового студента: "))
    grades[new_student] = new_grade
    del_student = input("Введите имя студента для удаления: ")
    if del_student in grades:
        del grades[del_student]
    print(f"Обновленный словарь: {grades}")

# Task 6: Check if numbers are even or odd
def task6():
    numbers = [10, 15, 20, 25, 30]
    for number in numbers:
        if number % 2 == 0:
            print(f"{number} — четное число")
        else:
            print(f"{number} — нечетное число")

# Task 7: Find maximum number in a list
def find_max(lst):
    max_num = lst[0]
    for num in lst:
        if num > max_num:
            max_num = num
    return max_num

def task7():
    numbers = [10, 20, 5, 30, 15]
    print(f"Максимальное число: {find_max(numbers)}")

# Task 8: Create a list of squares
def task8():
    squares = [i ** 2 for i in range(1, 11)]
    print(f"Список квадратов: {squares}")

# Task 9: Dictionary with user info
def task9():
    users = {'Alice': 22, 'Bob': 25, 'Charlie': 30}
    print(f"Исходный словарь: {users}")
    new_user = input("Введите имя нового пользователя: ")
    new_age = int(input("Введите возраст нового пользователя: "))
    users[new_user] = new_age
    del_user = input("Введите имя пользователя для удаления: ")
    if del_user in users:
        del users[del_user]
    print(f"Обновленный словарь: {users}")

# Task 10: Search value in dictionary
def task10():
    info = {'Alice': 22, 'Bob': 25, 'Charlie': 30}
    key = input("Введите имя для поиска: ")
    if key in info:
        print(f"Возраст {key}: {info[key]}")
    else:
        print("Имя не найдено.")

# Task 11: Check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def task11():
    num = int(input("Введите число для проверки на простое: "))
    if is_prime(num):
        print(f"{num} — простое число")
    else:
        print(f"{num} — не простое число")

# Task 12: Function to return square of a number
def square(n):
    return n ** 2

def task12():
    num = int(input("Введите число для возведения в квадрат: "))
    print(f"Квадрат числа {num}: {square(num)}")

# Task 13: Remove numbers less than 10 from a list
def task13():
    numbers = [5, 15, 3, 20, 8]
    numbers = [num for num in numbers if num >= 10]
    print(f"Список после удаления чисел меньше 10: {numbers}")

# Task 14: Count vowels in a string
def task14():
    text = input("Введите строку: ")
    vowels = "AEIOUaeiou"
    count = sum(1 for char in text if char in vowels)
    print(f"Количество гласных: {count}")

# Task 15: Dictionary with products and prices
def task15():
    products = {'apple': 50, 'banana': 30, 'orange': 40}
    print(f"Исходный словарь: {products}")
    new_product = input("Введите название нового продукта: ")
    new_price = int(input("Введите цену нового продукта: "))
    products[new_product] = new_price
    update_product = input("Введите название продукта для обновления цены: ")
    if update_product in products:
        new_price = int(input("Введите новую цену: "))
        products[update_product] = new_price
    print(f"Обновленный словарь: {products}")

# Task 16: Sum of values in a dictionary
def task16():
    values = {'a': 10, 'b': 20, 'c': 30}
    total_sum = sum(values.values())
    print(f"Сумма значений: {total_sum}")

# Task 17: Generate multiplication table
def task17():
    for i in range(1, 6):
        for j in range(1, 6):
            print(f"{i} x {j} = {i * j}", end="\t")
        print()

# Task 18: List of even numbers
def task18():
    evens = [num for num in range(1, 21) if num % 2 == 0]
    print(f"Список четных чисел: {evens}")

# Task 19: Dictionary with names and ages
def task19():
    people = {'Alice': 22, 'Bob': 25, 'Charlie': 30}
    for name, age in people.items():
        if age > 18:
            print(f"{name} старше 18 лет")

# Task 20: Function to calculate sum of numbers in a range
def sum_range(start, end):
    total = sum(range(start, end + 1))
    return total

def task20():
    start = int(input("Введите начальное значение диапазона: "))
    end = int(input("Введите конечное значение диапазона: "))
    print(f"Сумма чисел от {start} до {end}: {sum_range(start, end)}")

# Run all tasks
def main():
    print("Задание 1:")
    task1()
    print("\nЗадание 2:")
    task2()
    print("\nЗадание 3:")
    task3()
    print("\nЗадание 4:")
    task4()
    print("\nЗадание 5:")
    task5()
    print("\nЗадание 6:")
    task6()
    print("\nЗадание 7:")
    task7()
    print("\nЗадание 8:")
    task8()
    print("\nЗадание 9:")
    task9()
    print("\nЗадание 10:")
    task10()
    print("\nЗадание 11:")
    task11()
    print("\nЗадание 12:")
    task12()
    print("\nЗадание 13:")
    task13()
    print("\nЗадание 14:")
    task14()
    print("\nЗадание 15:")
    task15()
    print("\nЗадание 16:")
    task16()
    print("\nЗадание 17:")
    task17()
    print("\nЗадание 18:")
    task18()
    print("\nЗадание 19:")
    task19()
    print("\nЗадание 20:")
    task20()

if __name__ == "__main__":
    main()

