player_name = input()
best_player = ""
highest_score = goals_scored = 0
hattrick = False
while player_name != "END":
    goals_scored = int(input())
    if goals_scored > highest_score:
        highest_score = goals_scored
        best_player = player_name
        if goals_scored >= 3:
            hattrick = True
    if goals_scored >= 10:
        break
    player_name = input()

print(f'{best_player} is the best player!')
if hattrick is True:
    print(f"He has scored {highest_score} goals and made a hat-trick !!!")
else:
    print(f"He has scored {highest_score} goals.")
