# 1. Create a list of compony  (at list 4 compony) with input function and then remove the last one
compony_1 = input("Game 1: ")
compony_2 = input("Game 2: ")
compony_3 = input("Game 3: ")
compony_4 = input("Game 4: ")

games = []
games.append(compony_1)
games.append(compony_2)
games.append(compony_3)
games.append(compony_4)

print(games)

# 2
# Создай пустой список fruits. Запроси у пользователя ввести название фрукта и добавь его в список. Повтори это 5 раз, после чего выведи весь список.
fruits = []
for _ in range(5):
    fruit = input("Введите название фрукта: ")
    fruits.append(fruit)
print(fruits)

#  Создай список numbers с числами от 1 до 10. Запроси у пользователя ввести число, удали это число из списка и выведи обновленный список.
numbers = [1,2,3,4,5,6,7,8,9]
num_to_remove = int(input("Введите число для удаления из списка: "))
if num_to_remove in numbers:
    numbers.remove(num_to_remove)
print(numbers)

# Создай список animals с именами животных: "кошка", "собака", "кролик". Запроси у пользователя ввести еще одно животное и добавь его в список. Затем выведи все животные по одному в каждой строке.

animals = ["кошка", "собака", "кролик"]
new_animal = input("Введите название еще одного животного: ")
animals.append(new_animal)
for animal in animals:
    print(animal)
# Создай список colors с цветами: "красный", "зеленый", "синий". Запроси у пользователя ввести два дополнительных цвета и добавь их в список. Выведи количество цветов в списке.
colors = ["красный", "зеленый", "синий"]
color1 = input("Введите первый дополнительный цвет: ")
color2 = input("Введите второй дополнительный цвет: ")
colors.append(color1)
colors.append(color2)
print("Количество цветов в списке:", len(colors))
# Создай список grades с оценками: 3, 4, 5, 2, 5. Запроси у пользователя ввести оценку и добавь ее в список. Выведи среднее значение оценок.
grades = [3, 4, 5, 2, 5]
new_grade = int(input("Введите новую оценку: "))
grades.append(new_grade)
average = sum(grades) / len(grades)
print("Средняя оценка:", average)

