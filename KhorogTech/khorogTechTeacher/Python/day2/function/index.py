# Напиши функцию calculate_force, которая принимает массу и ускорение в качестве аргументов и вычисляет силу по формуле 
# F=m×a. Выведи результат.
def calculate_force(mass, acceleration):
    force = mass * acceleration
    print(f"Сила (F) равна {force} Н.")

# Запрос массы и ускорения у пользователя и вызов функции
mass = int(input("Введите массу (в килограммах): "))
acceleration = int(input("Введите ускорение (в м/с^2): "))
calculate_force(mass, acceleration)

# Напиши функцию calculate_rectangle_area, которая принимает длину и ширину прямоугольника и вычисляет его площадь по формуле 
# A=l×w. Выведи результат.
def calculate_rectangle_area(length, width):
    area = length * width
    print(f"Площадь прямоугольника равна {area} квадратных метров.")

# Запрос длины и ширины у пользователя и вызов функции
length = float(input("Введите длину прямоугольника (в метрах): "))
width = float(input("Введите ширину прямоугольника (в метрах): "))
calculate_rectangle_area(length, width)
