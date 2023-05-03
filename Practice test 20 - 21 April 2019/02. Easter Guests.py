from math import ceil

guests = int(input())
budget = int(input())
pie_cost = 4
egg_cost = 0.45

pies_needed = ceil(guests / 3)
eggs_needed = guests * 2
total_cost = (pie_cost * pies_needed) + (eggs_needed * egg_cost)

if budget >= total_cost:
    print(f"Lyubo bought {pies_needed} Easter bread and {eggs_needed} eggs.")
    print(f"He has {budget - total_cost:.2f} lv. left.")
else:
    print(f"Lyubo doesn't have enough money.")
    print(f"He needs {total_cost - budget:.2f} lv. more.")