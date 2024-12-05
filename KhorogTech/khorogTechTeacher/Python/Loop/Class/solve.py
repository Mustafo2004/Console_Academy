# Task 1: Запросить у пользователя число `n` и напечатать все числа от 1 до `n`.
n = int(input("Введите число n: "))
for i in range(1, n+1):
    print(i)

print()  

# Task 2: Запросить у пользователя строку и напечатать каждый символ этой строки.
string = input("Введите строку: ")
for char in string:
    print(char)

print()  

# Task 3: Запросить у пользователя число `n` и напечатать строку 'Привет' `n` раз.
n = int(input("Введите число n: "))
for i in range(n):
    print("Привет")

print()  

# Task 4: Запросить у пользователя два числа `a` и `b` и напечатать все числа от `a` до `b`.
a = int(input("Введите число a: "))
b = int(input("Введите число b: "))
for i in range(a, b+1):
    print(i)

print()  

# Task 5: Запросить у пользователя слово и напечатать его 3 раза.
word = input("Введите слово: ")
for i in range(3):
    print(word)

print()  

# Task 6: Запросить у пользователя строку и напечатать каждый ее символ в верхнем регистре.
string = input("Введите строку: ")
for char in string:
    print(char.upper())

print()  

# Task 7: Запросить у пользователя число `n` и напечатать все четные числа от 1 до `n`.
n = int(input("Введите число n: "))
for i in range(2, n+1, 2):
    print(i)

print()  

# Task 8: Запросить у пользователя число `n` и напечатать строку 'Python' `n` раз.
n = int(input("Введите число n: "))
for i in range(n):
    print("Python")

print()  

# Task 9: Запросить у пользователя строку и напечатать каждый второй символ этой строки.
string = input("Введите строку: ")
for i in range(1, len(string), 2):
    print(string[i])

print()  

# Task 10: Запросить у пользователя число `n` и напечатать все числа от `n` до 1 в обратном порядке.
n = int(input("Введите число n: "))
for i in range(n, 0, -1):
    print(i)

print()  

# Task 11: Запросить у пользователя строку и напечатать все гласные буквы в этой строке.
string = input("Введите строку: ")
vowels = "аеёиоуыэюяАЕЁИОУЫЭЮЯ"
for char in string:
    if char in vowels:
        print(char)

print()  

# Task 12: Запросить у пользователя число `n` и напечатать все числа от 1 до `n`, которые делятся на 3.
n = int(input("Введите число n: "))
for i in range(1, n+1):
    if i % 3 == 0:
        print(i)

print()  

# Task 13: Запросить у пользователя два числа `a` и `b` и напечатать все нечетные числа от `a` до `b`.
a = int(input("Введите число a: "))
b = int(input("Введите число b: "))
for i in range(a, b+1):
    if i % 2 != 0:
        print(i)

print()  

# Task 14: Запросить у пользователя строку и напечатать каждый символ этой строки с индексом.
string = input("Введите строку: ")
for i, char in enumerate(string):
    print(f"{i}: {char}")

print()  

# Task 15: Запросить у пользователя число `n` и напечатать все числа от 1 до `n`, которые делятся на 5.
n = int(input("Введите число n: "))
for i in range(1, n+1):
    if i % 5 == 0:
        print(i)

print()  

# Task 16: Запросить у пользователя строку и напечатать все согласные буквы в этой строке.
string = input("Введите строку: ")
consonants = "бвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩ"
for char in string:
    if char in consonants:
        print(char)

print()  

# Task 17: Запросить у пользователя число `n` и напечатать строку 'Кодинг' `n` раз.
n = int(input("Введите число n: "))
for i in range(n):
    print("Кодинг")

print()  

# Task 18: Запросить у пользователя строку и напечатать все цифры в этой строке.
string = input("Введите строку: ")
for char in string:
    if char.isdigit():
        print(char)

print()  

# Task 19: Запросить у пользователя два числа `a` и `b` и напечатать все числа от `a` до `b`, которые делятся на 2.
a = int(input("Введите число a: "))
b = int(input("Введите число b: "))
for i in range(a, b+1):
    if i % 2 == 0:
        print(i)

print()  

# Task 20: Запросить у пользователя строку и напечатать каждый символ этой строки в обратном порядке.
string = input("Введите строку: ")
for char in reversed(string):
    print(char)
