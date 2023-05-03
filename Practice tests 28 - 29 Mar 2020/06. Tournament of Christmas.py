days_tournament = int(input())
money_earned_for_current_day = total_money_earned = total_games_per_day = wins_per_day = total_money_earned_per_day = 0
total_winning_days = 0
score = ()

for i in range(1, days_tournament + 1):
    game_type = input()
    while game_type != "Finish":
        score = input()
        total_games_per_day += 1
        if score == "win":
            money_earned_for_current_day += 20
            wins_per_day += 1

        game_type = input()

    if game_type == "Finish":
        if wins_per_day > total_games_per_day / 2:
            money_earned_for_current_day = money_earned_for_current_day * 1.1
            total_winning_days += 1

        total_money_earned_per_day += money_earned_for_current_day
        total_money_earned += total_money_earned_per_day

    money_earned_for_current_day = total_games_per_day = wins_per_day = total_money_earned_per_day = 0

if total_winning_days > days_tournament / 2:
    print(f'You won the tournament! Total raised money: {(total_money_earned * 1.2):.2f}')
else:
    print(f'You lost the tournament! Total raised money: {total_money_earned:.2f}')
