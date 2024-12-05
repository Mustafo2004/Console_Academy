# Напиши программу, которая запрашивает у пользователя строку и выводит количество гласных букв в этой строке. Гласными считаются: "a", "e", "i", "o", "u".
vowels = "aeiouAEIOU"
user_string = input("Введите строку: ")
vowel_count = 0

for char in user_string:
    if char in vowels:
        vowel_count += 1

print("Количество гласных в строке:", vowel_count)

# Напиши программу, которая запрашивает у пользователя три числа и выводит их сумму.
total = 0

for _ in range(3):
    number = int(input("Введите число: "))
    total += number

print("Сумма чисел:", total)
