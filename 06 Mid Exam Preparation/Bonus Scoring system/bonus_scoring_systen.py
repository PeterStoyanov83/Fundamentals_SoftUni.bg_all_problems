import math

number_of_students = int(input())
number_of_total_lectures = int(input())
additional_bonus_points = int(input())
max_bonus_student = 0
student_attendance = 0
for student in range(1,number_of_students + 1 ):
    current_student_attendance = int(input())
    current_student_bonus = math.ceil(current_student_attendance / number_of_total_lectures * (5 + additional_bonus_points))
    if current_student_bonus > max_bonus_student:
        max_bonus_student = current_student_bonus
        student_attendance = current_student_attendance

print(f"Max Bonus: {max_bonus_student}.")
print(f'The student has attended {student_attendance} lectures.')