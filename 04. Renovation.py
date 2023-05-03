from math import ceil

h = int(input())
w = int(input())
percent_not_paint = int(input()) / 100

area_to_paint = ceil((h * w * 4) - (h * w * 4 * percent_not_paint))
painting = input()

while painting != "Tired!":
    condition_checker = area_to_paint
    area_to_paint -= int(painting)

    if area_to_paint <= 0:
        print(f'All walls are painted and you have {abs(area_to_paint)} l paint left!')
        if int(painting) - condition_checker == 0:
            print("All walls are painted! Great job, Pesho!")
        break
    painting = input()

if painting == "Tired!":
    print(f'{area_to_paint} quadratic m left.')
