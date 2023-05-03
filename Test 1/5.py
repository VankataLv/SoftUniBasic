user_command = str(input())
current_best_player = ""
current_high_score = 0
current_player = ""
hattrick_status = False
goals_scored = 0

while user_command != "END":
    current_player = user_command
    goals_scored = int(input())
    if goals_scored > current_high_score:
        current_high_score = goals_scored
        current_best_player = current_player
    if goals_scored >= 3:
        hattrick_status = True
    if goals_scored >= 10:
        break
    user_command = str(input())

print(f"{current_best_player} is the best player!")

if hattrick_status:
    print(f"He has scored {current_high_score} goals and made a hat-trick !!!")
else:
    print(f"He has scored {current_high_score} goals.")
