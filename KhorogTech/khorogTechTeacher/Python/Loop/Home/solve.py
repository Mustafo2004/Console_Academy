# Task 1: Напечатать числа от 1 до 10.
for i in range(1, 11):
    print(i)

print()  

# Task 2: Напечатать квадраты чисел от 1 до 5.
for i in range(1, 6):
    print(i ** 2)

print()  

# Task 3: Напечатать элементы списка fruits = ['яблоко', 'банан', 'вишня'].
fruits = ['яблоко', 'банан', 'вишня']
for fruit in fruits:
    print(fruit)

print()  

# Task 4: Напечатать буквы в слове word = 'python'.
word = 'python'
for letter in word:
    print(letter)

print()  

# Task 5: Напечатать только четные числа от 1 до 10.
for i in range(1, 11):
    if i % 2 == 0:
        print(i)

print()  

# Task 6: Напечатать элементы списка numbers = [5, 10, 15, 20, 25].
numbers = [5, 10, 15, 20, 25]
for number in numbers:
    print(number)

print()  

# Task 7: Напечатать все числа от 10 до 1 в обратном порядке.
for i in range(10, 0, -1):
    print(i)

print()  

# Task 8: Напечатать каждый второй элемент списка names = ['Анна', 'Борис', 'Виктор', 'Галина', 'Дмитрий'].
names = ['Анна', 'Борис', 'Виктор', 'Галина', 'Дмитрий']
for i in range(1, len(names), 2):
    print(names[i])

print()  

# Task 9: Напечатать длину каждого слова в списке words = ['кошка', 'собака', 'слон', 'жираф'].
words = ['кошка', 'собака', 'слон', 'жираф']
for word in words:
    print(len(word))

print()  

# Task 10: Напечатать сумму чисел от 1 до 10.
total = 0
for i in range(1, 11):
    total += i
print(total)

print()  

# Task 11: Напечатать произведение чисел от 1 до 5.
product = 1
for i in range(1, 6):
    product *= i
print(product)

print()  

# Task 12: Напечатать элементы списка colors = ['красный', 'синий', 'зеленый', 'желтый', 'черный'] с их индексами.
colors = ['красный', 'синий', 'зеленый', 'желтый', 'черный']
for index, color in enumerate(colors):
    print(index, color)

print()  

# Task 13: Напечатать все числа от 1 до 20, которые делятся на 3 без остатка.
for i in range(1, 21):
    if i % 3 == 0:
        print(i)

print()  

# Task 14: Напечатать каждый элемент списка temperatures = [23, 17, 25, 30, 22] умноженный на 2.
temperatures = [23, 17, 25, 30, 22]
for temp in temperatures:
    print(temp * 2)

print()  

# Task 15: Напечатать все буквы в строке text = 'Программирование это весело', кроме пробелов.
text = 'Программирование это весело'
for char in text:
    if char != ' ':
        print(char)

print()  

# Task 16: Напечатать все числа от 1 до 100, которые делятся на 10 без остатка.
for i in range(1, 101):
    if i % 10 == 0:
        print(i)

print()  

# Task 17: Напечатать каждую букву строки message = 'Hello, World!' в верхнем регистре.
message = 'Hello, World!'
for char in message:
    print(char.upper())

print()  

# Task 18: Напечатать индексы всех элементов списка cities = ['Москва', 'Лондон', 'Париж', 'Берлин'].
cities = ['Москва', 'Лондон', 'Париж', 'Берлин']
for index in range(len(cities)):
    print(index)

print()  

# Task 19: Напечатать все элементы списка numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], которые больше 5.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for number in numbers:
    if number > 5:
        print(number)

print()  

# Task 20: Напечатать все числа от 1 до 50, которые являются четными.
for i in range(1, 51):
    if i % 2 == 0:
        print(i)
