total_games_sold = int(input())
h_sold = f_sold = o_sold = others_sold = 0
for i in range(1, total_games_sold + 1):
    game_name = input()

    if game_name == "Hearthstone":
        h_sold += 1
    elif game_name == "Fornite":
        f_sold += 1
    elif game_name == "Overwatch":
        o_sold += 1
    else:
        others_sold += 1

print(f'Hearthstone - {(h_sold/total_games_sold) * 100:.2f}%')
print(f'Fornite - {(f_sold/total_games_sold) * 100:.2f}%')
print(f'Overwatch - {(o_sold/total_games_sold) * 100:.2f}%')
print(f'Others - {(others_sold/total_games_sold) * 100:.2f}%')

