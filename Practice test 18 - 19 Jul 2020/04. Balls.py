from math import floor

balls = int(input())
red = orange = yellow = white = other = black = total_points = other_colors = 0

for i in range(0, balls):
    picked_ball = input()
    if picked_ball == "red":
        total_points += 5
        red += 1
    elif picked_ball == "orange":
        total_points += 10
        orange += 1
    elif picked_ball == "yellow":
        total_points += 15
        yellow += 1
    elif picked_ball == "white":
        total_points += 20
        white += 1
    elif picked_ball == "black":
        total_points = floor(total_points / 2)
        black += 1
    else:
        other_colors += 1

print(f"Total points: {total_points}\n"
      f"Red balls: {red}\n"
      f"Orange balls: {orange}\n"
      f"Yellow balls: {yellow}\n"
      f"White balls: {white}\n"
      f"Other colors picked: {other_colors}\n"
      f"Divides from black balls: {black}")
