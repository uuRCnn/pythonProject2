import random

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

student_scroes = {student: random.randint(1, 100) for student in names}
passed_students = {student: score for (student, score) in student_scroes.items() if score >= 60}
print(passed_students)