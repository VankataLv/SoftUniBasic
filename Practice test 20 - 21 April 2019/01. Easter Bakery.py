flour_price_kg = float(input())
qty_flour = float(input())
qty_sugar = float(input())
qty_eggs_carton = int(input())
packets_maia = int(input())

sugar_price_kg = 0.75 * flour_price_kg
egg_price_carton = 1.1 * flour_price_kg
maia_price = 0.2 * sugar_price_kg

total_cost = (flour_price_kg * qty_flour) + (sugar_price_kg * qty_sugar) + (egg_price_carton * qty_eggs_carton) + (packets_maia * maia_price)

print(f'{total_cost:.2f}')