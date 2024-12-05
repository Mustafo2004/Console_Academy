# 1. Create a dictionary with input function for Phone : name , memory , camera year , price
phone_name = input("phone name: ")
phone_price = int(input("phone price: "))
phone_memory = int(input("phone memory: "))
phone_camera = int(input("phone camera: "))
phone_year = int(input("phone year: "))

phone = {
    "name": phone_name,
    "price": phone_price,
    "memory":phone_memory,
    "camera":phone_camera,
    "year":phone_year
}

print(phone)

# 2. Add new teacher to a existing dictionary 
teachers = {
    "Murtazo": 19,
    "Jahonngir": 22,
    "Masrur": 21
}

teacher_name = input("New student name: ")
teacher_age = input("New student age: ")

teachers[teacher_name] = teacher_age

del teachers["Masrur"]
print(teachers)
