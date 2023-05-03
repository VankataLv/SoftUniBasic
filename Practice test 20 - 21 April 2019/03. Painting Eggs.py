profit_factory = total_costs = price_per_egg = 0
egg_size = input()
egg_color = input()
egg_qty = int(input())

if egg_size == "Large":
    if egg_color == "Red":
        price_per_egg = 16
    elif egg_color == "Green":
        price_per_egg = 12
    elif egg_color == "Yellow":
        price_per_egg = 9
elif egg_size == "Medium":
    if egg_color == "Red":
        price_per_egg = 13
    elif egg_color == "Green":
        price_per_egg = 9
    elif egg_color == "Yellow":
        price_per_egg = 7
elif egg_size == "Small":
    if egg_color == "Red":
        price_per_egg = 9
    elif egg_color == "Green":
        price_per_egg = 8
    elif egg_color == "Yellow":
        price_per_egg = 5

total_costs = price_per_egg * egg_qty
profit_factory = total_costs * 0.65

print(f"{profit_factory:.2f} leva.")
