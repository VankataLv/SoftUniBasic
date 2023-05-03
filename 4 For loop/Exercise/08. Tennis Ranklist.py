from math import floor
tournaments_played = int(input())
initial_points = int(input())
tournament_points = total_points = current_points = tournaments_won = 0

for tournament in range(0, tournaments_played):
    tournament_finish = input()
    if tournament_finish == "W":
        current_points = 2000
        tournament_points += current_points
        total_points += current_points
        tournaments_won += 1
    elif tournament_finish == "F":
        current_points = 1200
        tournament_points += current_points
        total_points += current_points
    elif tournament_finish == "SF":
        current_points = 720
        tournament_points += current_points
        total_points += current_points

total_points += initial_points
print(f'Final points: {total_points}')
print(f'Average points: {floor(tournament_points / tournaments_played)}')
print(f'{(tournaments_won / tournaments_played) * 100:.2f}%')
