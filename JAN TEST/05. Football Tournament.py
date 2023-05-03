team_name = input()
games_played = int(input())
total_points = 0
wins = draws = losses = 0

if games_played == 0:
    print(f"{team_name} hasn't played any games during this season.")

else:
    for current_round in range(1, games_played + 1):
        result_game = input()
        if result_game == "W":
            total_points += 3
            wins += 1
        elif result_game == "D":
            total_points += 1
            draws += 1
        else:
            losses += 1

    print(f'{team_name} has won {total_points} points during this season.')
    print(f'Total stats:')
    print(f'## W: {wins}')
    print(f'## D: {draws}')
    print(f'## L: {losses}')
    print(f'Win rate: {(wins / games_played) * 100:.2f}%')
