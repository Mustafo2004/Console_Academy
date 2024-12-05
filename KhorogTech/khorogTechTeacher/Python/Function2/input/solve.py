import math

# Задача 1
def get_sum_of_three_numbers():
    a = float(input("Введите первое число: "))
    b = float(input("Введите второе число: "))
    c = float(input("Введите третье число: "))
    return a + b + c

# Задача 2
def get_difference_of_three_numbers():
    a = float(input("Введите первое число: "))
    b = float(input("Введите второе число: "))
    c = float(input("Введите третье число: "))
    return a - (b + c)

# Задача 3
def get_product_of_three_numbers():
    a = float(input("Введите первое число: "))
    b = float(input("Введите второе число: "))
    c = float(input("Введите третье число: "))
    return a * b * c

# Задача 4
def get_quotient_of_three_numbers():
    a = float(input("Введите первое число: "))
    b = float(input("Введите второе число: "))
    c = float(input("Введите третье число: "))
    if b != 0 and c != 0:
        return a / (b * c)
    else:
        return "Ошибка: деление на ноль"

# Задача 5
def get_square_root_from_input():
    a = float(input("Введите число: "))
    return math.sqrt(a)

# Задача 6
def get_cubic_root_from_input():
    a = float(input("Введите число: "))
    return a ** (1/3)

# Задача 7
def get_logarithm_from_input():
    a = float(input("Введите число: "))
    if a > 0:
        return math.log10(a)
    else:
        return "Ошибка: логарифм определен только для положительных чисел"

# Задача 8
def get_exponential_from_input():
    a = float(input("Введите число: "))
    return math.exp(a)

# Задача 9
def get_trapezoid_area_from_input():
    a = float(input("Введите длину первого основания трапеции: "))
    b = float(input("Введите длину второго основания трапеции: "))
    h = float(input("Введите высоту трапеции: "))
    return 0.5 * (a + b) * h

# Задача 10
def get_parallelogram_area_from_input():
    base = float(input("Введите длину основания параллелограмма: "))
    height = float(input("Введите высоту параллелограмма: "))
    return base * height

# Задача 11
def get_cylinder_volume_from_input():
    radius = float(input("Введите радиус основания цилиндра: "))
    height = float(input("Введите высоту цилиндра: "))
    return 3.14 * radius ** 2 * height

# Задача 12
def get_cone_volume_from_input():
    radius = float(input("Введите радиус основания конуса: "))
    height = float(input("Введите высоту конуса: "))
    return (1/3) * 3.14 * radius ** 2 * height

# Задача 13
def get_sphere_volume_from_input():
    radius = float(input("Введите радиус сферы: "))
    return (4/3) * 3.14 * radius ** 3

# Задача 14
def get_sphere_surface_area_from_input():
    radius = float(input("Введите радиус сферы: "))
    return 4 * 3.14 * radius ** 2

# Задача 15
def get_surface_area_of_cuboid_from_input():
    length = float(input("Введите длину параллелепипеда: "))
    width = float(input("Введите ширину параллелепипеда: "))
    height = float(input("Введите высоту параллелепипеда: "))
    return 2 * (length * width + width * height + height * length)

# Задача 16
def get_perimeter_of_polygon_from_input():
    number_of_sides = int(input("Введите количество сторон многоугольника: "))
    side_length = float(input("Введите длину одной стороны многоугольника: "))
    return number_of_sides * side_length

# Задача 17
def get_polygon_area_from_input():
    number_of_sides = int(input("Введите количество сторон многоугольника: "))
    side_length = float(input("Введите длину стороны многоугольника: "))
    return (number_of_sides * side_length ** 2) / (4 * math.tan(math.pi / number_of_sides))

# Задача 18
def get_angle_sum_of_polygon_from_input():
    number_of_sides = int(input("Введите количество сторон многоугольника: "))
    return (number_of_sides - 2) * 180

# Задача 19
def get_angle_of_polygon_from_input():
    number_of_sides = int(input("Введите количество сторон многоугольника: "))
    return 180 * (number_of_sides - 2) / number_of_sides

# Задача 20
def get_average_speed_from_input():
    distance = float(input("Введите расстояние (в км): "))
    time = float(input("Введите время (в часах): "))
    if time != 0:
        return distance / time
    else:
        return "Ошибка: время не может быть равно нулю"
