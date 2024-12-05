
# !ClassRoomJournala
studentsList = []

def add_students():
    count_students = int(input("How many students do you want to add? "))
    for _ in range(count_students):
        student_name = input("What is the student's name? ")
        math_score = int(input("What is the score in math? "))  
        draw_score = int(input("What is the score in draw? "))
        history_score = int(input("What is the score in history? "))
        computer_science_score = int(input("What is the score in computer science? "))
        
        student_dict = {
            "name": student_name,
            "math": math_score,
            "draw": draw_score,
            "history": history_score,
            "computer_science": computer_science_score
        }
        studentsList.append(student_dict)
    print("Students added:")
    for student in studentsList:
        print(student)

def remove_student():
    student_name = input("Which student do you want to remove? ")
    found = False
    for student in studentsList:
        if student["name"] == student_name:
            studentsList.remove(student)
            found = True
            break
    if found:
        print(f"Student {student_name} removed.")
    else:
        print(f"No student found with the name {student_name}")
    print("Updated students list:")
    for student in studentsList:
        print(student)

def update_student():
    student_name = input("Which student's record do you want to update? ")
    found = False
    for student in studentsList:
        if student["name"] == student_name:
            student["math"] = int(input("Enter the new score in math: "))
            student["draw"] = int(input("Enter the new score in draw: "))
            student["history"] = int(input("Enter the new score in history: "))
            student["computer_science"] = int(input("Enter the new score in computer science: "))
            print(f"Record updated for {student_name}:")
            print(student)
            found = True
            break
    if not found:
        print(f"No student found with the name {student_name}")

def find_student():
    student_name = input("Enter the name of the student you want to find: ")
    found = False
    for student in studentsList:
        if student["name"] == student_name:
            print(f"Record found for {student_name}:")
            print(student)
            found = True
            break
    if not found:
        print(f"No student found with the name {student_name}")

def calculate_average_scores():
    if len(studentsList) > 0:
        print("Average scores for each student:")
        for student in studentsList:
            total_score = (student["math"] + student["draw"] + student["history"] + student["computer_science"])
            average_score = total_score / 4
            print(f"{student['name']} - Average Score: {average_score:.2f}")
    else:
        print("No students in the list.")

# Example usage:
add_students()
remove_student()
update_student()
find_student()
calculate_average_scores()
