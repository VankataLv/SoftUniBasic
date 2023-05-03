jury_qty = int(input())
presentation_name = input()
current_presentation_grade = total_grade = sum_grades_for_current_presentation = 0
presentation_counter = 0

while presentation_name != "Finish":
    for grade in range(1, jury_qty + 1):
        current_presentation_grade = float(input())
        sum_grades_for_current_presentation += current_presentation_grade
    sum_grades_for_current_presentation /= jury_qty
    total_grade += sum_grades_for_current_presentation
    print(f"{presentation_name} - {sum_grades_for_current_presentation:.2f}.")
    sum_grades_for_current_presentation = 0
    presentation_counter += 1
    presentation_name = input()

if presentation_name == "Finish":
    print(f"Student's final assessment is {total_grade / presentation_counter:.2f}.")
