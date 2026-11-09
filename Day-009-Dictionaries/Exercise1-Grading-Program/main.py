student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}

students_grades = {}

for key in student_scores:
    student_score = student_scores[key]
    student_grade = ""

    if student_score > 90:
        student_grade = "Outstanding"
    elif student_score > 80:
        student_grade = "Exceeds Expectations"
    elif student_score > 70:
        student_grade = "Acceptable"
    else:
        student_grade = "Fail"
    students_grades[key] = student_grade

print(students_grades)
