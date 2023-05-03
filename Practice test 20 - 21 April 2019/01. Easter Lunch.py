qty_pies = int(input())
qty_eggs_cartons = int(input())
kg_cookies = int(input())
total_cost = 0
paint_cost_egg = 0.15 * 12
cookie_cost = 5.4
egg_cost = 4.35
pie = 3.2

total_cost = (qty_pies * pie) + ((paint_cost_egg * qty_eggs_cartons) + qty_eggs_cartons * egg_cost) + (cookie_cost * kg_cookies)

print(f"{total_cost:.2f}")