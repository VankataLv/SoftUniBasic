pie_qty = int(input())
best_baker = ""
current_baker_score = max_baker_score = current_judge_score = 0

for pie in range(0, pie_qty):
    current_baker_score = 0
    baker_name = input()
    current_judge_score = input()
    while str(current_judge_score) != "Stop":
        current_judge_score = int(current_judge_score)
        current_baker_score += current_judge_score
        current_judge_score = input()
    if str(current_judge_score) == "Stop":
        print(f'{baker_name} has {current_baker_score} points.')
        if current_baker_score > max_baker_score:
            max_baker_score = current_baker_score
            best_baker = baker_name
        if baker_name == best_baker:
            print(f"{baker_name} is the new number 1!")
print(f"{best_baker} won competition with {max_baker_score} points!")
