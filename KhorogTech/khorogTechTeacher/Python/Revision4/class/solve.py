# Task 1
def calculate(a, b):
    return a + b

result = calculate(5, 7)
numbers = []
numbers.append(result)
numbers.remove(result)
print("Task 1:", numbers)


# Task 2
student = {
    'name': 'Ivan',
    'age': 13,
    'grade': 'B'
}

def update_grade(student_dict, new_grade):
    student_dict['grade'] = new_grade

update_grade(student, 'A')
print("Task 2:", student)


# Task 3
def process_list(lst, num):
    if num in lst:
        lst.remove(num)
    else:
        lst.append(num)

numbers_list = [1, 2, 3, 4, 5]
process_list(numbers_list, 3)
print("Task 3:", numbers_list)
process_list(numbers_list, 6)
print("Task 3:", numbers_list)


# Task 4
inventory = {
    'item_name': 'Apple',
    'quantity': 10
}

def add_item(inventory_dict, item_name, quantity):
    inventory_dict[item_name] = quantity

def remove_item(inventory_dict, item_name):
    if item_name in inventory_dict:
        del inventory_dict[item_name]

add_item(inventory, 'Banana', 5)
print("Task 4:", inventory)
remove_item(inventory, 'Apple')
print("Task 4:", inventory)


# Task 5
def check_number(num):
    if num > 0:
        return "Положительное"
    elif num < 0:
        return "Отрицательное"
    else:
        return "Ноль"

print("Task 5:", check_number(10))
print("Task 5:", check_number(-5))
print("Task 5:", check_number(0))


# Task 6
def modify_list(lst, string):
    if string.startswith('A'):
        lst.append(string)
    elif string.startswith('B'):
        if string in lst:
            lst.remove(string)

strings_list = ['Apple', 'Banana', 'Cherry']
modify_list(strings_list, 'Apricot')
print("Task 6:", strings_list)
modify_list(strings_list, 'Banana')
print("Task 6:", strings_list)


# Task 7
person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 17
}

def update_age(person_dict):
    person_dict['age'] += 1
    if person_dict['age'] < 18:
        print("Task 7: Age is less than 18")

update_age(person)
print("Task 7:", person)


# Task 8
def calculate_area(length, width):
    return length * width

rectangles = {
    'rectangle1': calculate_area(5, 10),
    'rectangle2': calculate_area(3, 7)
}
print("Task 8:", rectangles)


# Task 9
def filter_list(lst):
    return [num for num in lst if num % 2 == 0]

numbers_list = [1, 2, 3, 4, 5, 6, 7, 8]
filtered_list = filter_list(numbers_list)
print("Task 9:", filtered_list)


# Task 10
book = {
    'title': 'Python Programming',
    'author': 'John Smith',
    'year': 2020
}

def change_author(book_dict, new_author):
    book_dict['author'] = new_author

change_author(book, 'Jane Doe')
print("Task 10:", book)
