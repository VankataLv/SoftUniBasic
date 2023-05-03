gr_food_bought = (int(input())) * 1000
food_eaten = input()
total_food_eaten = 0

while food_eaten != "Adopted":
    food_eaten = int(food_eaten)
    total_food_eaten += food_eaten
    food_eaten = input()

if total_food_eaten <= gr_food_bought:
    print(f'Food is enough! Leftovers: {gr_food_bought - total_food_eaten} grams.')
else:
    print(f'Food is not enough. You need {total_food_eaten - gr_food_bought} grams more.')
