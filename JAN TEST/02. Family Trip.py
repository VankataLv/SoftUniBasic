budget = float(input())
fuel_needed = float(input())
day = input()

price_liter_fuel = 2.1
price_guide = 100

fuel_cost = fuel_needed * price_liter_fuel
total_cost = fuel_cost + price_guide

if day == "Saturday":
    total_cost *= 0.9
else:
    total_cost *= 0.8

if budget >= total_cost:
    print(f'Safari time! Money left: {(budget - total_cost):.2f} lv.')
else:
    print(f'Not enough money! Money needed: {(total_cost - budget):.2f} lv.')
