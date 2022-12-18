# def gradingStudents(grades):
#     round_grades = []
#
#     for grade in grades:
#         grade = int(grade)
#
#         step_1 = int((grade + 5) / 5)
#         step_2 = step_1 * 5
#         step_3 = abs(grade - step_2)
#         print(f"grade: {grade}\n"
#               f"step_1: int(({grade} + 5) / 5) = {step_1}\n"
#               f"step_2: {step_1} * 5 = {step_2}\n"
#               f"step_3: {grade} - {step_2} = {step_3}")
#
#         diference = abs(grade - (int((grade + 5) / 5) * 5))
#         # print(grade, diference)
#         if 10 < grade:
#             if grade > 33 and diference < 3:
#                 round_grades.append(grade + diference)
#             else:
#                 round_grades.append(grade)
#     return round_grades
#


def gradingStudents(grades):
    round_grades = []
    index = 0
    for grade in range(grades[index]):
        index += 1
        diference = abs(grades[index] - (int((grades[index] + 5) / 5) * 5))
        if 33 <= grades[index]:
            if grades[index] > 33 and diference < 3:
                round_grades.append(grades[index] + diference)
            else:
                round_grades.append(grades[index])
    return round_grades


test_grades = [4, 73, 67, 38, 33]
# gradingStudents(test_grades)
[print(grade) for grade in gradingStudents(test_grades)]
