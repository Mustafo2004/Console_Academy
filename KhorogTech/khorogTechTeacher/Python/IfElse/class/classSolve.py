# Задача 1
# Напишите программу, которая запрашивает у пользователя число.
# Если число положительное, программа должна вывести "Число положительное".
# В противном случае - "Число не положительное".
num = float(input("Введите число: "))
if num > 0:
    print("Число положительное")
else:
    print("Число не положительное")

# Задача 2
# Напишите программу, которая запрашивает у пользователя возраст.
# Если возраст больше или равен 18, программа должна вывести "Вы совершеннолетний".
# В противном случае - "Вы несовершеннолетний".
age = int(input("Введите ваш возраст: "))
if age >= 18:
    print("Вы совершеннолетний")
else:
    print("Вы несовершеннолетний")

# Задача 3
# Напишите программу, которая запрашивает у пользователя два числа.
# Если первое число больше второго, программа должна вывести "Первое число больше".
# В противном случае - "Первое число не больше второго".
num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))
if num1 > num2:
    print("Первое число больше")
else:
    print("Первое число не больше второго")

# Задача 4
# Напишите программу, которая запрашивает у пользователя два числа.
# Если сумма чисел больше 10, программа должна вывести "Сумма больше 10".
# В противном случае - "Сумма не больше 10".
num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))
if num1 + num2 > 10:
    print("Сумма больше 10")
else:
    print("Сумма не больше 10")

# Задача 5
# Напишите программу, которая запрашивает у пользователя число.
# Если число четное, программа должна вывести "Число четное".
# В противном случае - "Число нечетное".
num = int(input("Введите число: "))
if num % 2 == 0:
    print("Число четное")
else:
    print("Число нечетное")

# Задача 6
# Напишите программу, которая запрашивает у пользователя букву.
# Если буква является гласной (a, e, i, o, u), программа должна вывести "Гласная буква".
# В противном случае - "Согласная буква".
letter = input("Введите букву: ").lower()
if letter in ('a', 'e', 'i', 'o', 'u'):
    print("Гласная буква")
else:
    print("Согласная буква")

# Задача 7
# Напишите программу, которая запрашивает у пользователя три числа.
# Если хотя бы одно из чисел отрицательное, программа должна вывести "Есть отрицательное число".
# В противном случае - "Нет отрицательных чисел".
num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))
num3 = float(input("Введите третье число: "))
if num1 < 0 or num2 < 0 or num3 < 0:
    print("Есть отрицательное число")
else:
    print("Нет отрицательных чисел")

# Задача 8
# Напишите программу, которая запрашивает у пользователя длину и ширину прямоугольника.
# Если длина равна ширине, программа должна вывести "Это квадрат".
# В противном случае - "Это прямоугольник".
length = float(input("Введите длину: "))
width = float(input("Введите ширину: "))
if length == width:
    print("Это квадрат")
else:
    print("Это прямоугольник")

# Задача 9
# Напишите программу, которая запрашивает у пользователя число.
# Если число делится на 5 без остатка, программа должна вывести "Число делится на 5".
# В противном случае - "Число не делится на 5".
num = int(input("Введите число: "))
if num % 5 == 0:
    print("Число делится на 5")
else:
    print("Число не делится на 5")

# Задача 10
# Напишите программу, которая запрашивает у пользователя строку.
# Если строка начинается с буквы "A", программа должна вывести "Строка начинается с буквы A".
# В противном случае - "Строка не начинается с буквы A".
string = input("Введите строку: ")
if string.startswith("A"):
    print("Строка начинается с буквы A")
else:
    print("Строка не начинается с буквы A")