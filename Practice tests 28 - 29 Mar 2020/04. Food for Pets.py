days = int(input())
amount_food_both = float(input())
total_food_eaten_dog = 0
total_food_eaten_cat = 0
biscuits_cat = biscuits_dog = biscuits_both = total_biscuits_both = 0

for i in range(1, days + 1):
    amount_food_dog = int(input())
    amount_food_cat = int(input())
    total_food_eaten_dog += amount_food_dog
    total_food_eaten_cat += amount_food_cat
    if i % 3 == 0:
        biscuits_dog = amount_food_dog * 0.1
        biscuits_cat = amount_food_cat * 0.1
        biscuits_both = biscuits_dog + biscuits_cat
        total_biscuits_both += biscuits_both

total_food_eaten_both = total_food_eaten_cat + total_food_eaten_dog
print(f'Total eaten biscuits: {round(total_biscuits_both)}gr.')
print(f'{((total_food_eaten_both / amount_food_both) * 100):.2f}% of the food has been eaten.')
print(f'{((total_food_eaten_dog / total_food_eaten_both) * 100):.2f}% eaten from the dog.')
print(f'{((total_food_eaten_cat / total_food_eaten_both) * 100):.2f}% eaten from the cat.')
