player_name = input()
player_number = 0
score_current_player = total_score_player = max_score = current_leader = 0

while player_name != "Stop":
    player_number += 1
    for letters in range(0, len(player_name)):
        player_guess = int(input())
        if player_guess == ord(player_name[letters]):
            score_current_player += 10
        else:
            score_current_player += 2

    total_score_player = score_current_player
    score_current_player = 0

    if max_score < total_score_player:
        max_score = total_score_player
        current_leader = player_name

    elif max_score == total_score_player:
        current_leader = player_name

    total_score_player = 0
    player_name = input()
    continue

print(f'The winner is {current_leader} with {max_score} points!')
