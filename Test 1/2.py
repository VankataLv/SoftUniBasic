from math import floor, ceil

days = int(input())
food_left = int(input())
food_needed_1 = float(input())
food_needed_2 = float(input())
food_needed_3 = float(input())

total_food_needed = (days * food_needed_1) + (days * food_needed_2) + (days * food_needed_3)

if food_left >= total_food_needed:
    print(f"{floor(food_left - total_food_needed)} kilos of food left.")

else:
    print(f"{ceil(total_food_needed - food_left)} more kilos of food are needed.")
