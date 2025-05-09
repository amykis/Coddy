'''
Create a function named analyze_grades that takes a dictionary of student grades as an argument.
The dictionary keys are student names, and the values are their corresponding grades.
The function should perform the following operations:

Calculate the average grade of all students.
Find the highest and lowest grades.
Identify the student(s) with the highest and lowest grades.
Return a dictionary containing the following information:
'average': The average grade (rounded to 2 decimal places)
'highest': The highest grade
'lowest': The lowest grade
'top_student': The name of the student with the highest grade
'bottom_student': The name of the student with the lowest grade
Test your function with the following dictionary:

student_grades = {'Alice': 85, 'Bob': 92, 'Charlie': 78, 'David': 95, 'Eve': 88}
Print the result of the function call.
'''


def analyze_grades(grades):
    # Write code here
    new_dict = {}
    average_all_student = sum(student_grades.values()) / len(student_grades)
    max_grades = max(student_grades.values())
    min_grades = min(student_grades.values())
    for el in student_grades:
        if student_grades[el] == max_grades:
            top_student = el
    for el in student_grades:
        if student_grades[el] == min_grades:
            bottom_student = el
    new_dict.update({"average": average_all_student, "highest": max_grades, "lowest": min_grades, "top_student": top_student, "bottom_student": bottom_student})
    return new_dict


# Test the function
student_grades = {'Alice': 85, 'Bob': 92, 'Charlie': 78, 'David': 95, 'Eve': 88}
result = analyze_grades(student_grades)
print(result)

'''
{'average': 87.6, 'highest': 95, 'lowest': 78, 'top_student': 'David', 'bottom_student': 'Charlie'}
'''