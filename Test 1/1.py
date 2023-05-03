per_fat = int(input()) / 100
per_pro = int(input()) / 100
per_car = int(input()) / 100
total_calories = int(input())
per_water = int(input()) / 100

total_grams_fat = (per_fat * total_calories) / 9
total_grams_pro = (per_pro * total_calories) / 4
total_grams_car = (per_car * total_calories) / 4
total_grams_food = total_grams_car + total_grams_pro + total_grams_fat
cal_per_gram = total_calories / total_grams_food
final = cal_per_gram * (1 - per_water)

print(f'{final:.4f}')