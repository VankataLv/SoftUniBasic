fail_grade_allowed = int(input())
problem_name = input()
problem_counter = sum_grades = fail_grade_counter = 0
last_problem = ""

while problem_name != "Enough":
    last_problem = problem_name
    problem_grade = int(input())
    if problem_grade > 4:
        problem_counter += 1
        sum_grades += problem_grade
        problem_name = input()

    else:
        fail_grade_counter += 1
        problem_counter += 1
        sum_grades += problem_grade
        if fail_grade_allowed <= fail_grade_counter:
            print(f'You need a break, {fail_grade_counter} poor grades.')
            quit()
        problem_name = input()
else:
    print(f'Average score: {sum_grades / problem_counter:.2f}')
    print(f'Number of problems: {problem_counter}')
    print(f'Last problem: {last_problem}')
