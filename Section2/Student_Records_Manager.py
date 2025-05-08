'''
Project Overview

The Student Records Manager manages student data using dictionaries and sets.
Each student record includes their name, age, grades, and courses.
Key operations include adding students, updating grades, checking course enrollment,
calculating average grades, listing students by course, and filtering top students based on grade thresholds.

This project demonstrates the practical use of dictionaries for structured data, sets to handle duplicates,
and advanced decision-making for efficient data management. It’s a practical way to apply Python concepts in a real-world scenario.


Challenge task5

Easy
Create a function named calculate_average_grade that takes one argument: name (string). The function should:

Check if the student name exists in the student_records dictionary.
If it does not exist, print "Student '<name>' not found." and return None.
If the name exists, calculate the average of the grades in the student's grades set.
If the grades set is empty, return 0.
Otherwise, calculate and return the average grade as a float.
Add (replace) the following block of code at the bottom of your code:

add_student("Alice", 20, ["Math", "Physics"])
add_student("Bob", 22, ["Biology", "Chemistry"])
add_grade("Alice", 90)
add_grade("Alice", 85)
add_grade("Bob", 75)
print(calculate_average_grade("Alice"))  # Should return 87.5
print(calculate_average_grade("Bob"))  # Should return 75.0
print(calculate_average_grade("Charlie"))  # Non-existent student, should print message and return None
print(calculate_average_grade("Alice"))  # Should return 87.5 again
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
        return  average_grade


student_records = {}
add_student("Alice", 20, ["Math", "Physics"])
add_student("Bob", 22, ["Biology", "Chemistry"])
add_grade("Alice", 90)
add_grade("Alice", 85)
add_grade("Bob", 75)
print(calculate_average_grade("Alice"))  # Should return 87.5
print(calculate_average_grade("Bob"))  # Should return 75.0
print(calculate_average_grade("Charlie"))  # Non-existent student, should print message and return None
print(calculate_average_grade("Alice"))  # Should return 87.5 again

'''
Student 'Alice' added successfully.
Student 'Bob' added successfully.
Grade 90 added for student 'Alice'.
Grade 85 added for student 'Alice'.
Grade 75 added for student 'Bob'.
87.5
75.0
Student 'Charlie' not found.
None
87.5
'''
