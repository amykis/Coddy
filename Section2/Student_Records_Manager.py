'''
Project Overview

The Student Records Manager manages student data using dictionaries and sets.
Each student record includes their name, age, grades, and courses.
Key operations include adding students, updating grades, checking course enrollment,
calculating average grades, listing students by course, and filtering top students based on grade thresholds.

This project demonstrates the practical use of dictionaries for structured data, sets to handle duplicates,
and advanced decision-making for efficient data management. It’s a practical way to apply Python concepts in a real-world scenario.


Challenge task2

Easy
Create a function named add_student that takes three arguments: name (string), age (integer), and courses (a list of strings). The function should:

Check if the student name already exists in the student_records dictionary. If it does, print "Student '<name>' already exists.".
If the name does not exist, add it to student_records with age, an empty set for grades, and a set of courses.
Print "Student '<name>' added successfully.".
Add the following block of code at the bottom of your code:

add_student("Alice", 20, ["Math", "Physics"])
add_student("Bob", 22, ["Biology", "Chemistry"])
print(student_records)l be a key,
and their details (age, grades, and courses) will be stored as a nested dictionary.
'''


def add_student(name, age, courses):
    if name in student_records:
        print(f"Student '{name}' already exists.")
    else:
        student_records[name] = {"age": age, "grades": set(), "courses": courses}
        print(f"Student '{name}' added successfully.")


student_records = {}
add_student("Alice", 20, ["Math", "Physics"])
add_student("Bob", 22, ["Biology", "Chemistry"])
print(student_records)
