# Напиши программу, которая запрашивает у пользователя два числа и проверяет, какое из них больше. Выведи соответствующее сообщение.
number1 = int(input("Введите первое число: "))
number2 = int(input("Введите второе число: "))

if number1 > number2:
    print(f"Первое число ({number1}) больше второго ({number2}).")
elif number1 < number2:
    print(f"Второе число ({number2}) больше первого ({number1}).")
else:
    print("Числа равны.")
# Напиши программу, которая запрашивает у пользователя букву и проверяет, является ли она гласной (a, e, i, o, u). Выведи соответствующее сообщение.
letter = input("Введите букву: ").lower()

if letter in ['a', 'e', 'i', 'o', 'u']:
    print("Эта буква является гласной.")
else:
    print("Эта буква не является гласной.")
# Напиши программу, которая запрашивает у пользователя пароль и проверяет, совпадает ли он с заранее заданным паролем "secret". Выведи соответствующее сообщение
correct_password = "secret"
user_password = input("Введите пароль: ")

if user_password == correct_password:
    print("Доступ разрешен.")
else:
    print("Неверный пароль.")
