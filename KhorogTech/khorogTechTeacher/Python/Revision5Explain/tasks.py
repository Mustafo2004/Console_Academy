# ### Задание 6: Проверка чисел на четность
# **Описание:** Напишите программу, которая проверяет, являются ли числа в списке четными или нечетными.
# **Шаги:**
# 1. Создайте список с 5 числами. EvenNumber[]
# 2. Используйте цикл `for`, чтобы проверить каждое число.
# 3. Используйте `if-else`, чтобы определить четность числа и вывести соответствующее сообщение.
# 4 append EvenNumber wef
numbers = [10, 15,20,25,20]
EvenNumbers = []
for number in numbers:
    if number % 2 == 0:
        EvenNumbers.append(number)
    else:
        print(number)
