'''
Project Overview

The Student Records Manager manages student data using dictionaries and sets.
Each student record includes their name, age, grades, and courses.
Key operations include adding students, updating grades, checking course enrollment,
calculating average grades, listing students by course, and filtering top students based on grade thresholds.

This project demonstrates the practical use of dictionaries for structured data, sets to handle duplicates,
and advanced decision-making for efficient data management. It’s a practical way to apply Python concepts in a real-world scenario.


Challenge task3

Easy
Create a function named add_grade that takes two arguments: name (string) and grade (integer). The function should:

Check if the student name exists in the student_records dictionary.
If it does not exist, print "Student '<name>' not found.".
If the name exists, add the grade to the student's grades set.
Print "Grade <grade> added for student '<name>'.".
Add (replace) the following block of code at the bottom of your code:

add_student("Alice", 20, ["Math", "Physics"])
add_student("Bob", 22, ["Biology", "Chemistry"])
add_grade("Alice", 90)
add_grade("Alice", 85)
add_grade("Bob", 75)
add_grade("Charlie", 80)  # Non-existent student
print(student_records)
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
        student_records[name][grade] = grade
        print(f"Grade {grade} added for student '{name}'.")


student_records = {}
add_student("Alice", 20, ["Math", "Physics"])
add_student("Bob", 22, ["Biology", "Chemistry"])
add_grade("Alice", 90)
add_grade("Alice", 85)
add_grade("Bob", 75)
add_grade("Charlie", 80)  # Non-existent student
print(student_records)
