def task_1():
    nums = []
    for _ in range(10):
        num = int(input("Введите число: "))
        nums.append(num)
    squares = []
    for num in nums:
        squares.append(num ** 2)
    print("Числа:", nums)
    print("Квадраты:", squares)

def task_2():
    nums = []
    for _ in range(10):
        num = int(input("Введите число: "))
        nums.append(num)
    i = 0
    while i < len(nums):
        if nums[i] % 2 == 0:
            nums.pop(i)
        else:
            i += 1
    print("Обновленный список:", nums)

def task_3():
    nums = []
    for _ in range(10):
        num = int(input("Введите число: "))
        nums.append(num)
    total = 0
    for num in nums:
        total += num
    avg = total / len(nums)
    print("Сумма:", total)
    print("Среднее значение:", avg)

def task_4():
    nums = []
    while True:
        num = input("Введите число (или 'стоп' для завершения): ")
        if num.lower() == 'стоп':
            break
        nums.append(int(num))
    divisible_by_3 = []
    for num in nums:
        if num % 3 == 0:
            divisible_by_3.append(num)
    print("Числа, которые делятся на 3:", divisible_by_3)

def task_5():
    nums = []
    for _ in range(5):
        num = int(input("Введите число: "))
        nums.append(num)
    multiplied = []
    for num in nums:
        multiplied.append(num * 2)
    print("Числа:", nums)
    print("Умноженные на 2:", multiplied)

def task_6():
    ages = {}
    for _ in range(5):
        name = input("Введите имя: ")
        age = int(input("Введите возраст: "))
        ages[name] = age
    print("Словарь:", ages)

def task_7():
    ages = {
        "Иван": 20,
        "Мария": 22,
        "Анна": 19,
        "Сергей": 21,
        "Дмитрий": 23
    }
    name_to_delete = input("Введите имя для удаления: ")
    if name_to_delete in ages:
        del ages[name_to_delete]
    print("Обновленный словарь:", ages)

def task_8():
    ages = {
        "Иван": 20,
        "Мария": 22,
        "Анна": 19,
        "Сергей": 21,
        "Дмитрий": 23
    }
    total_age = 0
    for age in ages.values():
        total_age += age
    average_age = total_age / len(ages)
    print("Средний возраст:", average_age)

def task_9():
    vowels = "аеёиоуыэюяАЕЁИОУЫЭЮЯ"
    consonants = "бвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩ"
    string = input("Введите строку: ")
    vowel_count = 0
    consonant_count = 0
    for char in string:
        if char in vowels:
            vowel_count += 1
        elif char in consonants:
            consonant_count += 1
    print("Количество гласных:", vowel_count)
    print("Количество согласных:", consonant_count)

def task_10():
    word = input("Введите слово: ")
    if word == word[::-1]:
        print("Слово является палиндромом")
    else:
        print("Слово не является палиндромом")

def task_11():
    string = input("Введите строку: ")
    words = string.split()
    print("Количество слов в строке:", len(words))

def task_12():
    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))
    operation = input("Введите операцию (+, -, *, /): ")
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Ошибка: деление на ноль"
    else:
        result = "Ошибка: неизвестная операция"
    print("Результат:", result)

def task_13():
    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))
    if num1 > num2:
        print("Большее число:", num1)
    elif num2 > num1:
        print("Большее число:", num2)
    else:
        print("Числа равны")

def task_14():
    num = int(input("Введите число: "))
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                print("Число не является простым")
                break
        else:
            print("Число является простым")
    else:
        print("Число не является простым")

def task_15():
    def factorial(n):
        if n == 0 or n == 1:
            return 1
        else:
            return n * factorial(n - 1)

    num = int(input("Введите число: "))
    print("Факториал числа", num, "равен", factorial(num))

def task_16():
    def is_even(n):
        return n % 2 == 0

    num = int(input("Введите число: "))
    print("Число четное" if is_even(num) else "Число нечетное")

def task_17():
    def is_divisible(a, b):
        return a % b == 0

    num1 = int(input("Введите первое число: "))
    num2 = int(input("Введите второе число: "))
    print("Делится" if is_divisible(num1, num2) else "Не делится")

def task_18():
    string = input("Введите строку: ")
    words = string.split()
    print("Список слов:", words)

def task_19():
    start = int(input("Введите начальное значение: "))
    end = int(input("Введите конечное значение: "))
    squares = []
    for num in range(start, end + 1):
        squares.append(num ** 2)
    print("Список квадратов:", squares)

def task_20():
    ages = {
        "Иван": 20,
        "Мария": 22,
        "Анна": 19,
        "Сергей": 21,
        "Дмитрий": 23
    }
    name = input("Введите имя: ")
    if name in ages:
        print("Возраст:", ages[name])
    else:
        print("Имя не найдено")

def task_21():
    names = []
    for _ in range(5):
        name = input("Введите имя: ")
        names.append(name)
    lengths = []
    for name in names:
        lengths.append(len(name))
    print("Имена:", names)
    print("Длины имен:", lengths)

def task_22():
    names = []
    for _ in range(5):
        name = input("Введите имя: ")
        names.append(name)
    letter = input("Введите букву для удаления имен: ")
    i = 0
    while i < len(names):
        if letter in names[i]:
            names.pop(i)
        else:
            i += 1
    print("Обновленный список имен:", names)

def task_23():
    nums = []
    for _ in range(5):
        num = int(input("Введите число: "))
        nums.append(num)
    reversed_nums = nums[::-1]
    print("Числа:", nums)
    print("Обратный порядок:", reversed_nums)

def task_24():
    nums = []
    for _ in range(10):
        num = int(input("Введите число: "))
        nums.append(num)
    even_count = 0
    odd_count = 0
    for num in nums:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    print("Количество четных чисел:", even_count)
    print("Количество нечетных чисел:", odd_count)

def task_25():
    nums1 = []
    nums2 = []
    for _ in range(5):
        num = int(input("Введите число для первого списка: "))
        nums1.append(num)
    for _ in range(5):
        num = int(input("Введите число для второго списка: "))
        nums2.append(num)
    combined = nums1 + nums2
    print("Объединенный список:", combined)

def task_26():
    grades = {}
    for _ in range(5):
        name = input("Введите имя студента: ")
        grade = int(input("Введите оценку студента: "))
        grades[name] = grade
    print("Словарь оценок:", grades)

def task_27():
    grades = {
        "Иван":"dsafsda",
    }
