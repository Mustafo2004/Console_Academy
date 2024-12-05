# Задача 22: Удаление имен с определенной длиной
def task_22():
    names = []
    for _ in range(5):
        name = input("Введите имя: ")
        names.append(name)
    
    length_to_remove = int(input("Введите длину для удаления имен: "))
    
    filtered_names = []
    for name in names:
        if len(name) != length_to_remove:
            filtered_names.append(name)
    
    print("Обновленный список имен:", filtered_names)

# Задача 23: Создание списка нечетных чисел
def task_23():
    start = int(input("Введите начальное значение: "))
    end = int(input("Введите конечное значение: "))
    
    odd_numbers = []
    for num in range(start, end + 1):
        if num % 2 != 0:
            odd_numbers.append(num)
    
    print("Список нечетных чисел:", odd_numbers)

# Задача 24: Словарь с кубами чисел
def task_24():
    start = int(input("Введите начальное значение: "))
    end = int(input("Введите конечное значение: "))
    
    cubes_dict = {}
    for num in range(start, end + 1):
        cubes_dict[num] = num ** 3
    
    print("Словарь с кубами чисел:", cubes_dict)

# Задача 25: Функция для вычисления среднего
def calculate_average(nums):
    total = 0
    for num in nums:
        total += num
    return total / len(nums)

def task_25():
    nums = []
    for _ in range(5):
        num = float(input("Введите число: "))
        nums.append(num)
    
    avg = calculate_average(nums)
    print("Среднее значение:", avg)

# Задача 26: Функция для нахождения минимума и максимума
def find_min_max(nums):
    min_num = nums[0]
    max_num = nums[0]
    
    for num in nums:
        if num < min_num:
            min_num = num
        if num > max_num:
            max_num = num
    
    return min_num, max_num

def task_26():
    nums = []
    for _ in range(5):
        num = float(input("Введите число: "))
        nums.append(num)
    
    min_num, max_num = find_min_max(nums)
    print("Минимальное значение:", min_num)
    print("Максимальное значение:", max_num)

# Задача 27: Функция для подсчета согласных
def count_consonants(string):
    consonants = "бвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩ"
    consonant_count = 0
    
    for char in string:
        if char in consonants:
            consonant_count += 1
    
    return consonant_count

def task_27():
    string = input("Введите строку: ")
    consonant_count = count_consonants(string)
    print("Количество согласных:", consonant_count)

# Задача 28: Создание списка по шагу
def task_28():
    start = int(input("Введите начальное значение: "))
    end = int(input("Введите конечное значение: "))
    step = int(input("Введите шаг: "))
    
    step_list = []
    for num in range(start, end + 1, step):
        step_list.append(num)
    
    print("Список чисел по шагу:", step_list)

# Задача 29: Проверка на совершеннолетие
def task_29():
    age = int(input("Введите возраст: "))
    
    if age >= 18:
        print("Вы совершеннолетний.")
    else:
        print("Вы несовершеннолетний.")

# Задача 30: Словарь с именами и хобби
def task_30():
    hobbies = {}
    for _ in range(5):
        name = input("Введите имя: ")
        hobby = input("Введите хобби: ")
        hobbies[name] = hobby
    
    print("Словарь с именами и хобби:", hobbies)

# Запуск всех задач
task_22()
task_23()
task_24()
task_25()
task_26()
task_27()
task_28()
task_29()
task_30()
