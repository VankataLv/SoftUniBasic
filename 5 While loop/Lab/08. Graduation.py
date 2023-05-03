current_year = sum_grades = 0
name_student = input()
current_grade = float(input())
yellow_card = False

while current_year < 13:
    if current_grade >= 4:
        sum_grades += current_grade
        current_year += 1
    else:
        if yellow_card:
            current_year += 1
            print(f"{name_student} has been excluded at {current_year} grade")
            break
        else:
            yellow_card = True
    if current_year == 12:
        print(f"{name_student} graduated. Average grade: {(sum_grades / 12):.2f}")
        break
    else:
        current_grade = float(input())
