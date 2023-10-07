###UTF-8###


def calculate_average_grades(grades_list):
    average_grades = {}

    for student, grade in grades_list:
        if student in average_grades:
            average_grades[student].append(grade)
        else:
            average_grades[student] = [grade]

    for student, grades in average_grades.items():
        average = sum(grades) / len(grades)
        print(f"Средняя оценка для студента {student}: {average:.2f}")

# Тест 1
grades_data_1 = [("Иванов", 4), ("Петров", 5), ("Иванов", 3), ("Петров", 4)]
calculate_average_grades(grades_data_1)

# Тест 2
grades_data_2 = [("Сидоров", 3), ("Петров", 4), ("Сидоров", 5), ("Петров", 3)]
calculate_average_grades(grades_data_2)

# Тест 3
grades_data_3 = [("Иванов", 5), ("Сидоров", 4), ("Иванов", 4), ("Сидоров", 3)]
calculate_average_grades(grades_data_3)
