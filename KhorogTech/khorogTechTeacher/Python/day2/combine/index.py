# Напиши программу, которая запрашивает у пользователя 5 чисел, сохраняет их в список и вычисляет сумму положительных чисел и количество отрицательных чисел. Используй функции для подсчета положительных и отрицательных чисел.
def count_positive_numbers(numbers):
    count = 0
    for num in numbers:
        if num > 0:
            count += 1
    return count

def count_negative_numbers(numbers):
    count = 0
    for num in numbers:
        if num < 0:
            count += 1
    return count

numbers = []
for i in range(5):
    number = float(input(f"Введите число {i+1}: "))
    numbers.append(number)

positive_count = count_positive_numbers(numbers)
negative_count = count_negative_numbers(numbers)

print(f"Количество положительных чисел: {positive_count}")
print(f"Количество отрицательных чисел: {negative_count}")


# Напиши программу, которая запрашивает у пользователя 5 имен и сохраняет их в список. Используй функцию для проверки, есть ли имя в списке. Выведи сообщение о наличии или отсутствии имени.
def name_exists(names_list, name):
    if name in names_list:
        return True
    else:
        return False

names = []
for i in range(5):
    name = input(f"Введите имя {i+1}: ")
    names.append(name)

search_name = input("Введите имя для поиска: ")
if name_exists(names, search_name):
    print(f"Имя {search_name} присутствует в списке.")
else:
    print(f"Имя {search_name} отсутствует в списке.")
