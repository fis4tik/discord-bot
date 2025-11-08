
grades_input = input()


grades = list(map(float, grades_input.split()))


if grades:
    average_grade = sum(grades) / len(grades)
    print(f"Средний балл: {average_grade:.2f}")
else:
    print("Не введены оценки.")