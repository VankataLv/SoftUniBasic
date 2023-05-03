tournament_name = input()
games_tournament = 0
my_team_score = 0
op_team_score = 0
my_team_wins = op_team_wins = 0
while tournament_name != "End of tournaments":
    games_tournament = int(input())
    for game_count in range(1, games_tournament + 1):
        my_team_score = int(input())
        op_team_score = int(input())
        if my_team_score > op_team_score:
            print(f"Game {game_count} of tournament {tournament_name}: win with {abs(my_team_score - op_team_score)} points.")
            my_team_wins += 1
        else:
            print(f"Game {game_count} of tournament {tournament_name}: lost with {abs(my_team_score - op_team_score)} points.")
            op_team_wins += 1
    tournament_name = input()
    if tournament_name == "End of tournaments":
        break

total_games_played = my_team_wins + op_team_wins
print(f"{(my_team_wins / total_games_played) * 100:.2f}% matches win")
print(f"{(op_team_wins / total_games_played) * 100:.2f}% matches lost")
