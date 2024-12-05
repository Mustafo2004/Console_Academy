# 1. Create a dictionary with input  for car
car_name = input("Car name: ")
car_price = int(input("Car price: "))
car_numbers = int(input("Car numbers: "))

car = {
    "name": car_name,
    "price": car_price,
    "numbers": car_numbers
}

print(car)


# 2. Add new student to a existing dictionary a the second
students = {
    "Hasan": 19,
    "Mustafo": 21,
    "Sayod": 32
}

student_name = input("New student name: ")
student_age = input("New student age: ")

students[student_name] = student_age

del students["Mustafo"]
print(students)
