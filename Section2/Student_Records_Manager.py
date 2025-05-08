'''
Project Overview

The Student Records Manager manages student data using dictionaries and sets.
Each student record includes their name, age, grades, and courses.
Key operations include adding students, updating grades, checking course enrollment,
calculating average grades, listing students by course, and filtering top students based on grade thresholds.

This project demonstrates the practical use of dictionaries for structured data, sets to handle duplicates,
and advanced decision-making for efficient data management. It’s a practical way to apply Python concepts in a real-world scenario.


Challenge task6

Easy
Create a function named list_students_by_course that takes one argument: course (string). The function should:

Iterate through the student_records dictionary and find all students enrolled in the specified course.
Return a list of names of students who are enrolled in the course.
If no students are enrolled in the course, return an empty list.
Add (replace) the following block of code at the bottom of your code:

add_student("Alice", 20, ["Math", "Physics"])
add_student("Bob", 22, ["Math", "Biology"])
add_student("Diana", 23, ["Chemistry", "Physics"])
print(list_students_by_course("Math"))  # Should return ["Alice", "Bob"]
print(list_students_by_course("Physics"))  # Should return ["Alice", "Diana"]
print(list_students_by_course("Biology"))  # Should return ["Bob"]
print(list_students_by_course("History"))  # Should return an empty list
'''


def add_student(name, age, courses):
    if name in student_records:
        print(f"Student '{name}' already exists.")
    else:
        student_records[name] = {"age": age, "grades": set(), "courses": courses}
        print(f"Student '{name}' added successfully.")


def add_grade(name, grade):
    if name not in student_records:
        print(f"Student '{name}' not found.")
    else:
        student_records[name]["grades"].add(grade)
        print(f"Grade {grade} added for student '{name}'.")


def is_enrolled(name, course):
    if name not in student_records:
        print(f"Student '{name}' not found.")
        return False
    elif course in student_records[name]['courses']:
        return True
    else:
        return False


def calculate_average_grade(name):
    if name not in student_records:
        print(f"Student '{name}' not found.")
        return None
    elif len(student_records[name]["grades"]) == 0:
        return 0
    else:
        average_grade = sum(student_records[name]["grades"]) / len(student_records[name]["grades"])
        return average_grade


def list_students_by_course(course):
    list_students = []
    for name in student_records:
        if course in student_records[name]["courses"]:
            list_students.append(name)
    return list_students

student_records = {}
add_student("Alice", 20, ["Math", "Physics"])
add_student("Bob", 22, ["Math", "Biology"])
add_student("Diana", 23, ["Chemistry", "Physics"])
print(list_students_by_course("Math"))  # Should return ["Alice", "Bob"]
print(list_students_by_course("Physics"))  # Should return ["Alice", "Diana"]
print(list_students_by_course("Biology"))  # Should return ["Bob"]
print(list_students_by_course("History"))  # Should return an empty list

'''
Student 'Alice' added successfully.
Student 'Bob' added successfully.
Student 'Diana' added successfully.
['Alice', 'Bob']
['Alice', 'Diana']
['Bob']
[]
'''
