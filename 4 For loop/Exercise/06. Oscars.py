actor_name = input()
initial_points = float(input())
judges = int(input())
total_points = initial_points
for judge in range(0, judges):
    current_judge_name = input()
    current_judge_grade = float(input())
    total_points += (len(current_judge_name) * current_judge_grade) / 2
    if total_points > 1250.5:
        print(f'Congratulations, {actor_name} got a nominee for leading role with {total_points:.1f}!')
        quit()

print(f'Sorry, {actor_name} you need {1250.5 - total_points:.1f} more!')
